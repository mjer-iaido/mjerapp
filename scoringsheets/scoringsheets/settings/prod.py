from .common import *

DEBUG = False

ALLOWED_HOSTS = [
	'*',
	]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mjerapp',
        'USER': 'mjeriaido',
        'PASSWORD': '1muso2jikiden',
   }
}

INSTALLED_APPS += (
    'gunicorn',
)
