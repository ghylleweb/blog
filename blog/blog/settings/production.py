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