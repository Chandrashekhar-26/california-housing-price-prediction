# California Housing Price Prediction

This project leverages machine learning to predict housing prices based on various features such as the number of rooms, location, population, income, and more. It uses FastAPI for building the web application, Docker for containerization, and MLflow for tracking machine learning experiments.
Also it is integrated with prometheus and grafana to have a nice dashboard to monitor.
The main focus of this project is to use MLOps concepts and tools nicely to manage for a machine learning system.
## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Running the App](#running-the-app)
5. [Endpoints](#endpoints)
   - [POST /predict](#post-predict)
   - [GET /retrain](#get-retrain)
   - [GET /metrics](#get-metrics)
6. [Testing](#testing)
7. [Docker Setup](#docker-setup)
8. [MLflow Integration](#mlflow-integration)
9. [Grafana & Prometheus Integration](#grafana--prometheus-integration)
10. [Contributing](#contributing)
11. [License](#license)

---

## Project Overview

The California Housing Price Prediction application predicts the price of a house based on a set of features. The system uses a machine learning model trained on historical data of housing prices in California. This model is served through a FastAPI app and includes functionality to predict prices, retrain the model, and monitor metrics related to the prediction process.
Also it is integrated with prometheus and grafana to have a nice dashboard to monitor.
**The main focus of this project is to use MLOps concepts and tools nicely to manage for a machine learning system.**
---

## Features

- **Price Prediction**: Predicts the price of a house based on various factors, including the number of rooms, age of the house, median income, etc.
  
- **Model Retraining**: Allows for retraining the model when new data becomes available.

- **Best Model**: Finding best performing model programmatically and using it for predictions.
- 
- **Metrics Monitoring**: Exposes important metrics for monitoring model performance and prediction latency.

- **Dockerized Application**: The entire application, including the API, model, and database, is packaged in Docker containers for easy deployment.

- **MLflow Integration**: Tracks experiments and models using MLflow, providing version control and monitoring of the model training process.

- **Grafana and Prometheus Integration**: Provides a dashboard for monitoring metrics such as prediction requests, response times, and latency through Prometheus and Grafana.

- **CI/CD Pipeline Integration**: Integrated a github action CI/CD pipeline to lint, test and deploy the push image to docker hub

- **API Endpoints**:
  - `/predict`: Predict housing prices based on provided input data.
  - `/retrain`: Trigger the retraining process for the model.
  - `/metrics`: Exposes metrics for Prometheus to collect.
  - `/logs`: Exposes the logs for predictions which includes request and prediction result. 
---

## Installation

0. Prerequisites - Python, Docker and Git must be installed.

1. Clone the repository:
    ```bash
    git clone https://github.com/Chandrashekhar-26/california-housing-price-prediction.git
    cd california-housing-price-prediction
    ```

2. Create a virtual environment and install dependencies (Skip if Running in Docker):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Ubuntu 
    venv\Scripts\activate  # On Windows 
    pip install -r requirements.txt
    ```

---

## Running the App

1. Make sure "Docker Desktop" Application is up and Running

2. Build and Run in Docker
   ```bash
   docker-compose up --build
   ```

## Access Applications and Endpoints
1. Access application endpoints at following uri:
   1. Predict API endpoint: http://localhost:5001/app/api/v1/housing-price/predict
   2. Metrics API endpoint (Used by prometheus to query metrics): http://localhost:5001/app/api/v1/housing-price/metrics
   3. Retrain API endpoint: http://localhost:5001/app/api/v1/housing-price/retrain
   4. Logs API endpoint: http://localhost:5001/app/api/v1/housing-price/logs
2. Access Prometheus at : http://localhost:9090
3. Access Grafana at : http://localhost:3000
4. Access MLFlow at : http://localhost:5000