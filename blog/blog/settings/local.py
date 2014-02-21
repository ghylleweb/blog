from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ghyllebert',
        'USER': 'ghyllebert',
        'PASSWORD': os.environ['MYSQL_PASS'],
        'HOST': '/Applications/MAMP/tmp/mysql/mysql.sock',
        'PORT': '8889',
    }
}

DEBUG = True
TEMPLATE_DEBUG = True

#localhost base url
BASE_URL = "http://localhost:10000"

WSGI_APPLICATION = 'blog.wsgi.application'

INSTALLED_APPS += ('debug_toolbar',)
