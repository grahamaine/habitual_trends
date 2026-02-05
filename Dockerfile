# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies (needed for Reflex and Node.js setup)
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code
COPY . .

# Initialize Reflex (this installs the necessary frontend components)
RUN reflex init

# Export the frontend (this creates the production-ready JS/HTML)
# This will run the 'reflex export' command to bundle the UI
RUN reflex export --frontend-only --no-zip

# Expose the ports Reflex uses
# 3000 for the frontend UI, 8001 for the Reflex backend API
EXPOSE 3000 8001

# Run the app in production mode
CMD ["reflex", "run", "--env", "prod"]