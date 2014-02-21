from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ghyllebert',
        'USER': 'ghyllebert',
        'PASSWORD': os.environ['MYSQL_PASS'],
    }
}

WSGI_APPLICATION = 'blog.prod_wsgi.application'