from .base import *

DATABASES['default'] = DATABASES['dev']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

INSTALLED_APPS = INSTALLED_APPS + ['customauth.apps.CustomauthConfig',]
AUTH_USER_MODEL = 'customauth.Staff'
LOGIN_URL = '/login'