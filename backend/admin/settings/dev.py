from .base import *
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['*']

SECRET_KEY = "testsecret"

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

