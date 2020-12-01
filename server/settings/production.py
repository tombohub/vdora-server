from .base import *
import dj_database_url
import django_on_heroku

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {

    }
}

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)


# cookie setting
CSRF_COOKIE_SAMESITE = 'None'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SECURE = True

CSRF_TRUSTED_ORIGINS = ['dashboard.projectvdora.com']
CSRF_COOKIE_DOMAIN = 'dashboard.projectvdora.com'

# for Heroku
django_on_heroku.settings(locals())
