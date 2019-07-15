import os
from . import app_secrets
from .base import BASE_DIR, PROJECT_NAME

ALLOWED_HOSTS = app_secrets.ALLOWED_HOSTS

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': app_secrets.DB_NAME,
        'USER': app_secrets.DB_USER,
        'PASSWORD': app_secrets.DB_PASSWORD,
        'HOST': 'localhost',
        'PORT': '5432',
        'ATOMIC_REQUESTS': True,
    }
}

# Media files
MEDIA_ROOT = '/var/www/{}/media'.format(PROJECT_NAME)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':
        {
            'production': {
                'format': '%(asctime)s [%(levelname)s] %(process)d %(thread)d '  '%(pathname)s:%(lineno)d %(message)s'
            },
        },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': '/var/log/{}/app.log'.format(PROJECT_NAME),
            'formatter': 'production',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
