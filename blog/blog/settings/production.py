from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['ghyllebert.be']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ghyllebert',
        'USER': 'ghyllebert',
        'PASSWORD': os.environ['MYSQL_PASS'],
    }
}

WSGI_APPLICATION = 'blog.prod_wsgi.application'

STATIC_ROOT = "/home/ghyllebert/webapps/blog/repo/blog/static/"

EMAIL_HOST = 'smtp.webfaction.com'
EMAIL_HOST_USER = 'ghyllebert'
EMAIL_HOST_PASSWORD = os.environ['MAILBOX_PASS']
DEFAULT_FROM_EMAIL = 'jonas@ghyllebert.be'
SERVER_EMAIL = 'info@ghyllebert.be'

ADMINS = ('jonas@ghyllebert.be',)
MANAGERS = ADMINS

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'special': {
            '()': 'project.logging.SpecialFilter',
            'foo': 'bar',
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'filters': ['special']
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'myproject.custom': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
            'filters': ['special']
        }
    }
}