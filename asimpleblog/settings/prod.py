import os

import dj_database_url

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['asimpleblogapp.herokuapp.com']

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
