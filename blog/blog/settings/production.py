from .base import *

DEBUG = True
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['.ghyllebert.be', '.ghyllebert.be.']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ghyllebert',
        'USER': 'ghyllebert',
        'PASSWORD': os.environ['MYSQL_PASS'],
    }
}

WSGI_APPLICATION = 'blog.prod_wsgi.application'