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

SIMPLE_JWT_SIGNING_KEY=config("SIMPLE_JWT_SIGNING_KEY_P")


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(seconds=1000),
    'REFRESH_TOKEN_LIFETIME': timedelta(seconds=1000),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SIMPLE_JWT_SIGNING_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

