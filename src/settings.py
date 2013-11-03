# Django settings for src project.
#
# https://developers.google.com/cloud-sql/docs/django
#


import os, sys
from os.path import abspath, dirname, join

ALLOWED_HOSTS = [".apdsm.com", ".aproiowa.com", ".aproiowa.appspot.com"]
PROJECT_DIR = abspath(dirname(__file__))

LIB_DIR = join(PROJECT_DIR, 'lib')
if LIB_DIR not in sys.path:
    sys.path.insert(0, LIB_DIR)

ADMINS = (
    ("Aaron Madison", "aaron.l.madison@gmail.com"),
)

DATABASES = {
    'default': {
        'ENGINE': 'google.appengine.ext.django.backends.rdbms',
        'INSTANCE': 'twomadisons.com:tc-assistantpro:assistantpro',
        'NAME': 'assistantpro_txn',
    }
}

if (os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine') or
    os.getenv('SETTINGS_MODE') == 'prod'):
    # Running on production App Engine, so use a Google Cloud SQL database.
    DEBUG = False
    MANAGERS = (
        ('Linda Ruppert', 'linda.ruppert@assistantproiowa.com'),
    )
    EMAIL_BACKEND = 'djangoappengine.mail.AsyncEmailBackend'

    TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )),
    )

else:
    # local dev environment
    DEBUG = True
    MANAGERS = ADMINS
    EMAIL_BACKEND = 'djangoappengine.mail.EmailBackend'

    TEMPLATE_LOADERS = (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
    )


# Specify a queue name for the async. email backend
EMAIL_QUEUE_NAME = 'default'

TEMPLATE_DEBUG = DEBUG

# Email configuration
DEFAULT_FROM_EMAIL = 'noreply@assistantproiowa.com'

TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'

USE_I18N = False
USE_L10N = False

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = abspath(join(PROJECT_DIR, 'production_static'))
STATIC_URL = '/static/'
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_DIRS = (
    join(PROJECT_DIR, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'e!7j6@opp_d-2o%_o65i&kd0hw!%&($@9w3d$(a4l3opln-pz_'



MIDDLEWARE_CLASSES = (
    'google.appengine.ext.appstats.recording.AppStatsDjangoMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    join(PROJECT_DIR, 'templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.request",
    "django.contrib.messages.context_processors.messages",
)

INSTALLED_APPS = (
    'debug_toolbar',
    'django.contrib.staticfiles',

    'djbootstrap',
    'web',
)

INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
