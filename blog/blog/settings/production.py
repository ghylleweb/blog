from .base import *

DEBUG = True
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


#EMAIL_HOST = 'smtp.webfaction.com'
#EMAIL_HOST_USER = 'ghyllebert'
#EMAIL_HOST_PASSWORD = os.environ['MAILBOX_PASS']
#DEFAULT_FROM_EMAIL = 'jonas@ghyllebert.be'
#SERVER_EMAIL = 'info@ghyllebert.be'

#ADMINS = ('jonas@ghyllebert.be',)
#MANAGERS = ADMINS

