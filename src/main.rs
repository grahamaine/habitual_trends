use axum::{
    routing::{post, get},
    Router,
    Json,
};
use serde::{Deserialize, Serialize};
use tower_http::cors::{Any, CorsLayer};
use std::net::SocketAddr;
use tokio::net::TcpListener; // Need this now!

#[derive(Deserialize)]
struct LoginRequest {
    email: String,
}

#[derive(Serialize)]
struct LoginResponse {
    status: String,
    message: String,
}

#[tokio::main]
async fn main() {
    tracing_subscriber::fmt::init();
    println!("🚀 Starting Habitual Trends Backend...");

    let cors = CorsLayer::new()
        .allow_origin(Any)
        .allow_methods(Any)
        .allow_headers(Any);

    let app = Router::new()
        .route("/", get(|| async { "Backend is running!" }))
        .route("/api/login", post(login_handler))
        .layer(cors);

    // New way to start the server in Axum 0.7:
    let addr = SocketAddr::from(([127, 0, 0, 1], 3005));
    let listener = TcpListener::bind(addr).await.unwrap();
    
    println!("✅ SUCCESS: Server listening at http://{}", addr);

    axum::serve(listener, app).await.unwrap();
}

async fn login_handler(Json(payload): Json<LoginRequest>) -> Json<LoginResponse> {
    println!("Received login request for: {}", payload.email);
    
    Json(LoginResponse {
        status: "success".to_string(),
        message: format!("Welcome, {}!", payload.email),
    })
}