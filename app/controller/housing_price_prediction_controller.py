from app.service import housingPricePredictionService
from fastapi import Response
from fastapi import APIRouter
from app.schema import HousePricePredictionInput
from prometheus_client import Counter, Summary, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time


# Log Prometheus metrics
REQUEST_COUNT = Counter("total_prediction_requests", "Total number of prediction requests")
RESPONSE_TIME = Summary("prediction_response_time_seconds", "Time taken for prediction response")
REQUEST_LATENCY = Histogram("request_latency_seconds", "Latency per request", buckets=[0.1, 0.25, 0.5, 1, 2, 5])


housing_price_prediction_router = APIRouter(
    prefix="",
    tags=["predict housing price"]
)


@housing_price_prediction_router.post("/predict")
@RESPONSE_TIME.time()
def predict(input: HousePricePredictionInput):
    """It is to predict the House price based on the given data"""
    start_time = time.time()
    REQUEST_COUNT.inc()

    result = housingPricePredictionService.predict(input)

    duration = time.time() - start_time
    REQUEST_LATENCY.observe(duration)

    return result


@housing_price_prediction_router.get("/retrain")
def retrain():
    """ It is to retrain the model"""
    housingPricePredictionService.retrain()
    return f'Model retrain triggered'


@housing_price_prediction_router.get("/metrics")
def get_metric():
    """This is to get the metrics of API using prometheus"""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@housing_price_prediction_router.get("/logs")
def fetch_logs():
    """ This is to fetch the logs from sql lite"""
    return housingPricePredictionService.fetch_logs()
