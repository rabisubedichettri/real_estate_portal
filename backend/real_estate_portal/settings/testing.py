from decouple import config
from .base import *
DEBUG = False
SECRET_KEY = config('SECRET_KEY_T')
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config("DATABASE_NAME_T"),
        'USER': config("DATABASE_USER_T"),
        'PASSWORD': config("DATABASE_PASSWORD_T"),
        'HOST': config("DATABASE_HOST_ADDRESS_T"),
        'PORT': config("DATABASE_PORT_"),
    }
}
