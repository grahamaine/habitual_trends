use actix_cors::Cors;
use actix_web::{get, post, web, App, HttpResponse, HttpServer, Responder, http};
use serde::{Deserialize, Serialize};
use env_logger;

// --- 1. DATA STRUCTURES ---

#[derive(Deserialize)]
struct LoginRequest {
    email: String,
    password: String,
}

#[derive(Serialize)]
struct LoginResponse {
    message: String,
    token: Option<String>,
}

// This defines what a "Habit" looks like
#[derive(Serialize)]
struct Habit {
    id: i32,
    name: String,
    streak: i32,
    completed: bool,
}

// --- 2. API ROUTES ---

// Login Route (With Bypass for Testing)
#[post("/api/login")]
async fn login(req: web::Json<LoginRequest>) -> impl Responder {
    println!("Incoming login request for: {}", req.email);
    println!("DEBUG: Password received: '{}'", req.password);

    // BYPASS: Accepts "password123" OR any other password for now
    if req.password == "password123" || true {
        println!("✅ Login Successful");
        HttpResponse::Ok().json(LoginResponse {
            message: "Login successful!".to_string(),
            token: Some("abc-123-fake-token".to_string()),
        })
    } else {
        HttpResponse::Unauthorized().json(LoginResponse {
            message: "Invalid email or password".to_string(),
            token: None,
        })
    }
}

// Habits Route (Serves the list of habits)
#[get("/api/habits")]
async fn get_habits() -> impl Responder {
    println!("Fetching habits list...");
    
    // Fake data (We will replace this with a Database later)
    let habits = vec![
        Habit { id: 1, name: "Code Rust".to_string(), streak: 5, completed: true },
        Habit { id: 2, name: "Exercise".to_string(), streak: 12, completed: false },
        Habit { id: 3, name: "Read Books".to_string(), streak: 3, completed: false },
    ];

    HttpResponse::Ok().json(habits)
}

// --- 3. MAIN SERVER ---

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    // FIX: Wrapped in unsafe to prevent the crash error
    unsafe {
        std::env::set_var("RUST_LOG", "actix_web=info");
    }
    env_logger::init();

    // Note: We are now running on Port 8080!
    println!("🚀 Rust Backend running at http://localhost:8080");

    HttpServer::new(|| {
        let cors = Cors::default()
            .allowed_origin("http://localhost:3000") // Allow Reflex Frontend
            .allowed_methods(vec!["GET", "POST"])
            .allowed_headers(vec![http::header::AUTHORIZATION, http::header::ACCEPT])
            .allowed_header(http::header::CONTENT_TYPE)
            .max_age(3600);

        App::new()
            .wrap(cors) 
            .service(login)      // Register Login
            .service(get_habits) // Register Habits
    })
    .bind(("127.0.0.1", 8080))? // BIND TO 8080
    .run()
    .await
}