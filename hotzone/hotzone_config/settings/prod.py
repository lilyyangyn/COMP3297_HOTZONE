from .base import *

DATABASES['default'] = DATABASES['prod']

STATIC_ROOT=str(BASE_DIR.joinpath('static'))