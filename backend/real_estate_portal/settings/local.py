from decouple import config
from .base import *
from datetime import timedelta

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

SIMPLE_JWT_SIGNING_KEY=config("SIMPLE_JWT_SIGNING_KEY_L")

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

# Cors Settings
CORS_ALLOW_CREDENTIALS = False

# NOTE:
# change 'https://example-prod-react.com' to your frontend domain
CORS_ORIGIN_WHITELIST = []
