import os

import dj_database_url

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['asimpleblogapp.herokuapp.com']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
