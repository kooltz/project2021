from .base import *

DEBUG = False

ALLOWED_HOSTS = []

SECRET_KEY = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD':'',
        'HOST':'',
        'PORT':''
    }
}