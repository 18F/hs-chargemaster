import dj_database_url
from .base import *

DEBUG = True

DATABASES = {"default": dj_database_url.config(conn_max_age=600)}

INTERNAL_IPS = ['127.0.0.1']

MIDDLEWARE = MIDDLEWARE + ['debug_toolbar.middleware.DebugToolbarMiddleware']

INSTALLED_APPS = INSTALLED_APPS + ['debug_toolbar']
