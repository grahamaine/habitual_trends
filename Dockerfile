# Stage 1: Build the Rust Backend
FROM rust:1.75-slim as rust-builder
WORKDIR /app
COPY . .
RUN cargo build --release

# Stage 2: Build the Python/Reflex Frontend
FROM python:3.11-slim
WORKDIR /app

# Install system dependencies for Reflex
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Copy the compiled Rust binary from the first stage
COPY --from=rust-builder /app/target/release/habitual_backend /app/target/release/habitual_backend

# Initialize Reflex (this prepares the frontend)
RUN reflex init

# Expose the ports (8080 for Rust, 3000 for Reflex)
EXPOSE 8080
EXPOSE 3000

# Start both using a simple shell command (or use a process manager like foreman)
CMD /app/target/release/habitual_backend & python -m reflex run --env prod