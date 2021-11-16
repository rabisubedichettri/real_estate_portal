from decouple import config
from .base import *
DEBUG = False
SECRET_KEY = config('SECRET_KEY_L')
ALLOWED_HOSTS = ['127.0.0.1']
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config("DATABASE_NAME_L"),
        'USER': config("DATABASE_USER_L"),
        'PASSWORD': config("DATABASE_PASSWORD_L"),
        'HOST': config("DATABASE_HOST_ADDRESS_L"),
        'PORT': config("DATABASE_PORT_L"),
    }
}
