# Use official Python runtime
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY main.py .

# Expose port (Cloud Run defaults to 8080)
EXPOSE 8080

# Run with Gunicorn for production-grade performance
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:${SERVICE_PORT:-8080} main:app"]
