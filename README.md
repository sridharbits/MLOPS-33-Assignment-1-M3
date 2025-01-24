# MLflow Flask Application

This workspace contains a Flask application for serving an MLflow model to predict diabetes outcomes.

## File Structure
- `app.py`: Flask app to serve the MLflow model.
- `Dockerfile`: Dockerfile to containerize the application.
- `requirements.txt`: Python dependencies.

## Setup Instructions

### Build and Run with Docker
1. Build the Docker image:
   ```bash
   docker build -t mlflow-flask-app .
