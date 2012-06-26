# Django settings for eeditionautomate production enviroment.
from settings import *

DEBUG = TEMPLATE_DEBUG = Ture

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'aroberts_eeditionautomate',                      # Or path to database file if using sqlite3.
        'USER': 'aroberts',                      # Not used with sqlite3.
        'PASSWORD': 'cceafd9d',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


MEDIA_ROOT = ''

MEDIA_URL = ''

STATIC_ROOT = '/home/aroberts/webapps/static_media'

STATIC_URL = 'http://aroberts.webfactional.com/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    '/home/aroberts/webapps/eeditionautomate/static',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)



MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

TEMPLATE_DIRS = (
    '/home/anthony/eeditionautomate/templates'
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.admindocs',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
    'signup',
    'paypal.standard.ipn',
    'ckeditor',
)
PAYPAL_RECEIVER_EMAIL = "nns.ar_1334418630_biz@gmail.com"
SITE_NAME = 'enewsautomation.dyndns-mail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'aroberts'
EMAIL_HOST_PASSWORD = 'M@ximus01' # do not commit your settings file with your password in it. It would then be public on the web. Commit dummy text and change it immediately after. 
EMAIL_PORT = 587
EMAIL_USE_TLS = True
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            [      'Undo', 'Redo',
              '-', 'Bold', 'Italic', 'Underline',
              '-', 'Link', 'Unlink', 'Anchor',
              '-', 'Format',
              '-', 'SpellChecker', 'Scayt',
              '-', 'Maximize',
            ],
            [      'HorizontalRule',
              '-', 'Table',
              '-', 'BulletedList', 'NumberedList',
              '-', 'Cut','Copy','Paste','PasteText','PasteFromWord',
              '-', 'SpecialChar',
              '-', 'Source',
              '-', 'About',
            ]
        ],
        'width': 600,
        'height': 300,
        'toolbarCanCollapse': False,
    }
}


