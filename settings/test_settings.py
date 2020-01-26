from .basic_settings import *

#import sentry_sdk
#from sentry_sdk.integrations.django import DjangoIntegration

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n3@e^2c*&@%*cn4la&b$9^@w2oib5cc-l%n0(=taa#@sl#1$k6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'OPTIONS': {
            'options': '-c search_path=public'
            },
        'NAME': 'tesiscamilo',
        'USER': 'camilotest',
        'PASSWORD': 'camilotest',
        'HOST': 'database-camilo-test.cwmhlunep6tx.us-east-1.rds.amazonaws.com',
        'PORT': '5432',
        'CHARSET': 'UTF8',

    },
}

STATIC_URL = '/static/'