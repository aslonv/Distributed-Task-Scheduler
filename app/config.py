# app/config.py

import os

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
