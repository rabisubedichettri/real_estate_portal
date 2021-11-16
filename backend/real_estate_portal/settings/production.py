from decouple import config
from .base import *
DEBUG = False
SECRET_KEY = config('SECRET_KEY_P')
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config("DATABASE_NAME_P"),
        'USER': config("DATABASE_USER_P"),
        'PASSWORD': config("DATABASE_PASSWORD_P"),
        'HOST': config("DATABASE_HOST_ADDRESS_P"),
        'PORT': config("DATABASE_PORT_P"),
    }
}
