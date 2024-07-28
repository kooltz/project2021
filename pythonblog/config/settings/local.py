from .base import *

DEBUG = True

ALLOWED_HOSTS = []

INTERAL_IPS = ['127.0.0.1']

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

SECRET_KEY = '=ombg$$(*4f!tdt&=tcz*ee3jv5k0xceo4^@5(@2xanmvi$u$&'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'oc_sandb',
        'USER': 'kooltz',
        'PASSWORD':'qkfrks14',
        'HOST':'140.245.68.3',
        'PORT':'3306'
    }
}