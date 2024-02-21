from .base import *
import dj_database_url

DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = "testsecret"

DATABASES = {
        'default': dj_database_url.parse(os.getenv('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True),
    }

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIR = [
    BASE_DIR / 'static/'
]


STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS":{
            "access_key": os.getenv("ACCESS_KEY"),
            "secret_key": os.getenv("SECRET_KEY"),
            "bucket_name": os.getenv("BUCKET_NAME"),
            "region_name": os.getenv("REGION_NAME"),
            "endpoint_url": "http://localhost:4566",
            "object_parameters": {
                "CacheControl": "max-age=86400"
            },
        }
    },
    "staticfiles": 
        {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage"
        }
}
