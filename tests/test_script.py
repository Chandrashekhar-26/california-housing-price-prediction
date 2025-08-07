
def test_fun():
    assert True

# from fastapi.testclient import TestClient
# from app.controller import housing_price_prediction_router
#
#
# # Create a tests client to simulate API requests
# client = TestClient(housing_price_prediction_router)
#
#
# def test_retrain():
#     # Send GET request to /retrain endpoint
#     response = client.get("/retrain")
#
#     # Ensure the status code is 200 and the retraining message is returned
#     assert response.status_code == 200
#     assert response.text == "Model retrain triggered"
#
#
# def test_predict():
#     # Sample input to send in the POST request
#     input_data = {
#         "total_rooms": 1000,
#         "housing_median_age": 20,
#         "total_bedrooms": 3,
#         "population": 500,
#         "households": 200,
#         "median_income": 2.5,
#         "latitude": 37.77,
#         "longitude": -122.42
#     }
#
#     # Send POST request to /predict endpoint
#     response = client.post("/predict", json=input_data)
#
#     # Ensure the status code is 200
#     assert response.status_code == 200
#
#     # Check if the response contains the expected keys
#     assert "predicted_price" in response.json()
#     assert "model" in response.json()
#
#
# # Test the /metrics endpoint
# def test_metrics():
#     response = client.get("/metrics")
#
#     assert response.status_code == 200
#
#     assert response.headers["Content-Type"] == "text/plain; version=0.0.4; charset=utf-8"
#     assert "total_prediction_requests" in response.text
#     assert "prediction_response_time_seconds" in response.text
#     assert "request_latency_seconds" in response.text
