import os
from .base import *


SECRET_KEY = 'y8**ulu&88vqb57kab*h1(_34#)gqn1=h3k_9a4i#%%8otc*f='

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
