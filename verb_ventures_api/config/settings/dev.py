from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'verbventures_dev',
        'USER': 'vv_admin',
        'PASSWORD': dev_db_password,
        'HOST': 'verbventures.cud98scqn1pb.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
