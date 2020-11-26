from .base import *

DATABASES['default'] = DATABASES['dev']

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
