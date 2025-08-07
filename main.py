from fastapi.responses import RedirectResponse
from datetime import datetime
import uvicorn
import mlflow
import warnings
from app import create_app
from config import Config
from app.logger import RequestResponseLoggerMiddleware

# Set MLflow experiment on app start
print('******************* MLFLOW_EXPERIMENT')
mlflow_tracking_uri = Config.MLFLOW_TRACKING_URI
experiment_name = Config.MLFLOW_EXPERIMENT
mlflow.set_tracking_uri(mlflow_tracking_uri)

experiment = mlflow.get_experiment_by_name(experiment_name)
if experiment is None:
    experiment_id = mlflow.create_experiment(experiment_name)
mlflow.set_experiment(experiment_name)

app = create_app()

# add middleware to log request and responses
app.add_middleware(RequestResponseLoggerMiddleware)

# # Prometheus metrics
# REQUEST_COUNT = Counter("prediction_requests_total", "Total number of prediction requests")
# RESPONSE_TIME = Summary("prediction_response_time_seconds", "Time taken for prediction response")

# turn warnings off
warnings.filterwarnings("ignore")

@app.on_event("startup")
async def startup_event():
    print(f' ***** App Running')


@app.get('/')
def redirect_to():
    redirect_url = f'/{Config.BASE_URL}/{Config.API_VERSION}/info'
    return RedirectResponse(url=redirect_url)


@app.get(f'/{Config.BASE_URL}/{Config.API_VERSION}/info')
def get_info():
    return {
        'App': 'California Housing Prediction API',
        'Version': '1.0.0',
        'Time': datetime.now()
    }


# @app.post(f'/{Config.BASE_URL}/{Config.API_VERSION}/predict-housing-price')
# def predict_housing_price(request_body: dict):
#     print(request_body)
#     return {}


if __name__ == "__main__":
    uvicorn.run("main:app", host=Config.HOST, port=Config.PORT, reload=True)
