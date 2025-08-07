# California Housing Price Prediction

This project leverages machine learning to predict housing prices based on various features such as the number of rooms, location, population, income, and more. It uses FastAPI for building the web application, Docker for containerization, and MLflow for tracking machine learning experiments.

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

---

## Features

- **Price Prediction**: Predicts the price of a house based on various factors, including the number of rooms, age of the house, median income, etc.
  
- **Model Retraining**: Allows for retraining the model when new data becomes available.

- **Metrics Monitoring**: Exposes important metrics for monitoring model performance and prediction latency.

- **Dockerized Application**: The entire application, including the API, model, and database, is packaged in Docker containers for easy deployment.

- **MLflow Integration**: Tracks experiments and models using MLflow, providing version control and monitoring of the model training process.

- **Grafana and Prometheus Integration**: Provides a dashboard for monitoring metrics such as prediction requests, response times, and latency through Prometheus and Grafana.

- **API Endpoints**:
  - `/predict`: Predict housing prices based on provided input data.
  - `/retrain`: Trigger the retraining process for the model.
  - `/metrics`: Exposes metrics for Prometheus to collect.

---

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/california-housing-price-prediction.git
    cd california-housing-price-prediction
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

---

## Running the App

You can run the FastAPI app locally using the following command:

```bash
uvicorn app.main:app --reload
