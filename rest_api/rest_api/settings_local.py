DEBUG = True

DATABASES = {
        'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': 'pgperffarm-db',
                'USER': 'postgres',
                'PASSWORD': 'password',
                'HOST': '/var/run/postgresql'
                #'HOST': '/raid'
                }
        }

PGAUTH_REDIRECT = ''
PGAUTH_KEY = ''

PROJECT_PATH = '/var/www/rest_api/'
PGAUTH_REDIRECT = ''
PGAUTH_KEY = ''

EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''  # individual smtp password