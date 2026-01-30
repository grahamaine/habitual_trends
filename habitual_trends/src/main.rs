use axum::{
    routing::get,
    Router,
    Json,
};
use serde::Serialize;
use std::net::SocketAddr;
use tower_http::cors::{CorsLayer, Any};

// 1. Define the Data Structure (Matches your Python UI)
#[derive(Serialize)]
struct Habit {
    id: u32,
    name: String,
}

// 2. The Handler Function (What happens when you request data)
async fn get_habits() -> Json<Vec<Habit>> {
    let habits = vec![
        Habit { id: 1, name: "Rust Backend (Fetched from Rust!)".to_string() },
        Habit { id: 2, name: "Morning Run (From Rust)".to_string() },
        Habit { id: 3, name: "Deep Work (From Rust)".to_string() },
    ];
    Json(habits)
}

#[tokio::main]
async fn main() {
    // 3. Setup CORS (Crucial: Allows your Python app to talk to Rust)
    let cors = CorsLayer::new()
        .allow_origin(Any) // In production, replace 'Any' with your specific frontend URL
        .allow_methods(Any);

    // 4. Build the Router
    let app = Router::new()
        .route("/habits", get(get_habits))
        .layer(cors);

    // 5. Run the Server
    let addr = SocketAddr::from(([127, 0, 0, 1], 8080));
    println!("Rust Backend listening on http://{}", addr);
    
    let listener = tokio::net::TcpListener::bind(addr).await.unwrap();
    axum::serve(listener, app).await.unwrap();
}