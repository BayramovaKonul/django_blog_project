from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'db.sqlite3' 
    #  'default': env.db()  #takes database_url
    }}


AUTH_PASSWORD_VALIDATORS = [
  
]

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"