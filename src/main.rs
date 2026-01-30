// 1. Make sure your imports at the top include Path
use axum::{routing::get, extract::Path, Router, Json};
use serde_json::{json, Value};

#[tokio::main]
async fn main() {
    env_logger::init();

    // 2. Build the router inside your Rust file
    let app = Router::new()
        .route("/", get(|| async { "Hello, Habitual Trends!" }))
        // This is the line that was giving you the terminal error:
        .route("/api/trends/:username", get(get_user_trends));

    let listener = tokio::net::TcpListener::bind("127.0.0.1:3000").await.unwrap();
    println!("Listening on http://127.0.0.1:3000");
    
    axum::serve(listener, app).await.unwrap();
}

// 3. Add the handler function below main
async fn get_user_trends(Path(username): Path<String>) -> Json<Value> {
    Json(json!({
        "user": username,
        "trends": ["coding", "rust", "Entebbe-exploration"],
        "message": format!("Welcome, {}! Here are your trends.", username)
    }))
}