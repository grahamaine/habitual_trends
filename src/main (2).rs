use axum::{
    extract::{Path, State},
    routing::{get, post},
    Json, Router,
};
use log::{error, info};
use serde::{Deserialize, Serialize};
use sqlx::{sqlite::SqlitePool, FromRow};
use std::net::SocketAddr;
use tower_http::cors::{Any, CorsLayer};

// 1. Shared state for the database connection
#[derive(Clone)]
struct AppState {
    db: SqlitePool,
}

// 2. Data Models - Synchronized with your Python payload
#[derive(Serialize, Deserialize, FromRow, Debug)]
struct Habit {
    id: Option<i64>,
    user: String,
    habit_name: String,
    timestamp: Option<String>,
}

#[derive(Deserialize)]
struct CreateHabit {
    user: String,
    habit_name: String,
}

#[tokio::main]
async fn main() {
    // Initialize logging
    env_logger::Builder::from_env(env_logger::Env::default().default_filter_or("info")).init();
    info!("🚀 Starting Habitual Trends Backend...");

    // Windows-safe SQLite connection
    let database_url = "sqlite:data.db"; 
    let pool = match SqlitePool::connect(database_url).await {
        Ok(p) => p,
        Err(e) => {
            error!("❌ CRITICAL: Could not connect to data.db: {}", e);
            std::process::exit(1);
        }
    };

    // Initialize the habits table
    let _ = sqlx::query(
        "CREATE TABLE IF NOT EXISTS habits (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT NOT NULL,
            habit_name TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );"
    )
    .execute(&pool)
    .await;

    let state = AppState { db: pool };

    // CORS configuration - Vital for Python script access
    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods(Any)
        .allow_headers(Any);

    // 3. Routing - Matches Python's BASE_URL/api/habits and /api/trends
    let app = Router::new()
        .route("/", get(|| async { "Habitual Trends API Active" }))
        .route("/api/trends/:username", get(get_user_trends))
        .route("/api/habits", post(add_habit))
        .layer(cors)
        .with_state(state);

    // Using Port 3005 as confirmed in your terminal output
    let addr = SocketAddr::from(([127, 0, 0, 1], 3005));
    
    // Improved listener with error handling
    let listener = match tokio::net::TcpListener::bind(addr).await {
        Ok(l) => l,
        Err(e) if e.kind() == std::io::ErrorKind::AddrInUse => {
            error!("❌ Port 3005 is already in use!");
            info!("💡 Use 'Stop-Process -Name habitual-trends-backend' in PowerShell.");
            std::process::exit(1);
        }
        Err(e) => {
            error!("❌ Failed to bind to port: {}", e);
            std::process::exit(1);
        }
    };

    info!("✅ SUCCESS: Server listening at http://{}", addr);
    axum::serve(listener, app).await.unwrap();
}

// --- HANDLERS ---

// GET: Retrieve habits for a specific user
async fn get_user_trends(
    Path(username): Path<String>,
    State(state): State<AppState>,
) -> Json<Vec<Habit>> {
    info!("🔍 Querying trends for user: {}", username);
    let habits = sqlx::query_as::<_, Habit>("SELECT * FROM habits WHERE user = ? ORDER BY timestamp DESC")
        .bind(username)
        .fetch_all(&state.db)
        .await
        .unwrap_or_default();

    Json(habits)
}

// POST: Save a new habit from your Python script
async fn add_habit(
    State(state): State<AppState>,
    Json(payload): Json<CreateHabit>,
) -> Json<Habit> {
    info!("📝 Recording habit: '{}' for user: '{}'", payload.habit_name, payload.user);

    let res = sqlx::query("INSERT INTO habits (user, habit_name) VALUES (?, ?)")
        .bind(&payload.user)
        .bind(&payload.habit_name)
        .execute(&state.db)
        .await
        .expect("❌ Database Insert Failed");

    Json(Habit {
        id: Some(res.last_insert_rowid()),
        user: payload.user,
        habit_name: payload.habit_name,
        timestamp: Some("Just now".to_string()),
    })
}