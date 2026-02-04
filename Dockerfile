# Stage 1: The Builder
FROM rust:1.75-slim AS builder
WORKDIR /app
COPY . .
# Build only the release binary
RUN cargo build --release

# Stage 2: The Runtime (The "Lightweight" version)
FROM debian:bookworm-slim
WORKDIR /app

# Copy only the compiled binary from the builder
COPY --from=builder /app/target/release/habitual_trends .

# Set environment variables (e.g., for your Gemini API keys)
ENV RUST_LOG=info

# Expose the port your backend runs on
EXPOSE 8080

CMD ["./habitual_trends"]