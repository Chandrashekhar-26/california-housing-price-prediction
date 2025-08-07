from dotenv import dotenv_values
import os

env_path = os.path.join(os.path.dirname(__file__), '.env')
_properties = dotenv_values(env_path)


class Config:
    try:
        ENV = _properties['ENV']
        HOST = _properties['HOST']
        PORT = int(_properties['PORT'])
        BASE_URL = _properties['BASE_URL']
        API_VERSION = _properties['API_VERSION']
        MLFLOW_EXPERIMENT = _properties['MLFLOW_EXPERIMENT']
        MLFLOW_TRACKING_URI = _properties['MLFLOW_TRACKING_URI']
        LOG_DIR = _properties['LOG_DIR']
    except Exception as e:
        raise Exception(f'Invalid environment properties. Error: {e}')
