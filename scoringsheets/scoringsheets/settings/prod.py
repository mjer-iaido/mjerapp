from .common import *

DEBUG = False

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
    }
}

INSTALLED_APPS += (
    'gunicorn',
)
