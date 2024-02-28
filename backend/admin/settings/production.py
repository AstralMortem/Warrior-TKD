from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = os.getenv('ALLOWED_HOST').split(',')


DATABASES = {
        'default': dj_database_url.parse(os.getenv('DATABASE_URL'),
        conn_max_age=600,
        conn_health_checks=True),
    }


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
        "OPTIONS":{
            "access_key": os.getenv("ACCESS_KEY"),
            "secret_key": os.getenv("SECRET_KEY"),
            "bucket_name": os.getenv("BUCKET_NAME"),
            "region_name": os.getenv("REGION_NAME"),
            "endpoint_url": f"https://{os.getenv('REGION_NAME')}.digitaloceanspaces.com",
            "object_parameters": {
                "CacheControl": "max-age=86400"
            },
        }
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

CSRF_TRUSTED_ORIGINS = [
    'https://api.warrior-tkd.pp.ua'
]
