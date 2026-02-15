import os

MYSQL = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_ADDON_DB'),
        'USER': os.environ.get('MYSQL_ADDON_USER'),
        'PASSWORD': os.environ.get('MYSQL_ADDON_PASSWORD'),
        'HOST': os.environ.get('MYSQL_ADDON_HOST'),
        'PORT': os.environ.get('MYSQL_ADDON_PORT'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
