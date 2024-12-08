from .base import *

DEBUG = True

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
    'default': env.db()  #takes database_url
}



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

AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME='blogarticlesapp'
AWS_S3_CUSTOM_DOMAIN='%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS={
   'CacheControl': 'max-age=86400',
}
AWS_LOCATION='static'
STATIC_URL= 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN,AWS_LOCATION)


STORAGES = {
   "default": {
       "BACKEND": "config.storage_backend.MediaStorage",
   },
 
   "staticfiles": {
       "BACKEND": "storages.backends.s3boto3.S3StaticStorage",
   },
}

SECURE_SSL_REDIRECT=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=86400
SESSION_COOKIE_SECURE=True
SECURE_HSTS_PRELOAD=True
SECURE_HSTS_INCLUDE_SUBDOMAINS=True

