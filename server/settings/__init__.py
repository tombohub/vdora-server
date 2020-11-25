from decouple import config

if config('DJANGO_ENVIRONMENT') == 'development':
    from .development import *
else:
    from .production import *
