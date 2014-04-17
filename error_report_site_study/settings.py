# coding: utf-8

"""
Django settings for error_report_site_study project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'auz&psr_z-7w*(_z&$8vw4)ckthk_r_vw1^knq^n8q=jh%)xuy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'error_report_site_study.urls'

WSGI_APPLICATION = 'error_report_site_study.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

###################################################################################################

# Error Report 必要設定
DEBUG = False

# Error Report 必要設定：使用的 SMTP Server
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mic1028002@gmail.com'
EMAIL_HOST_PASSWORD = 'mffjafea753'
EMAIL_PORT = 587

# Error Report 必要設定：mail from
SERVER_EMAIL = 'mic1028002@gmail.com'

ALLOWED_HOSTS = ['*']

# Error Report 必要設定：mail to
# 這邊注意資料型態 ( ('name', 'mail'), ('name', 'mail'))
ADMINS = (('scott', 'mic1028002@gmail.com'),)

# 自製的 Error Reporter
DEFAULT_EXCEPTION_REPORTER_FILTER = 'error_report_site_study.my_reporter.handler'

# 自製 Logger ( Email Error Reporter 也是從這來的 )
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'NOTSET',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'NOTSET',
            'propagate': True,
        },
    },
}

###################################################################################################
