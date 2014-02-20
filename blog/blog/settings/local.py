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


#localhost base url
BASE_URL = "http://localhost:10000"


STATIC_ROOT = BASE_DIR.child("static")

CKEDITOR_UPLOAD_PATH = BASE_DIR.child("media")

INSTALLED_APPS += ('debug_toolbar',)

GUNICORN_PORT = 10000