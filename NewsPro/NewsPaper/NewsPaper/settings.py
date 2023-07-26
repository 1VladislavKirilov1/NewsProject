"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import logging

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&21pl-#(+*)*c(-)%8x(59lbv&nrh66=a7*m5k#fn1_2_x9_@+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOGGING = {
     'version': 1,
     'disable_existing_loggers': False,
     'style': '{',
     'formatters': {
         'debug': {
             'format': '%(levelname)s %(message)s %(asctime)s'
         },
         'warning': {
             'format': '%(levelname)s %(message)s %(asctime)s %(pathname)s'
         },
         'error': {
             'format': '%(levelname)s %(message)s %(asctime)s %(pathname)s %(exc_info)s'
         },
         'module': {
             'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
         },
         'security': {
             'format': '%(message)s %(asctime)s %(module)s %(levelname)s'
         }
     },
     'filters': {
         'require_debug_true': {
             '()': 'django.utils.log.RequireDebugTrue',
         },
         'require_debug_false': {
             '()': 'django.utils.log.RequireDebugFalse',
         },
     },
     'handlers': {
         'console': {
             'level': 'DEBUG',
             'filters': ['require_debug_true'],
             'class': 'logging.StreamHandler',
             'formatter': 'debug'
         },
         'file_info': {
             'level': 'INFO',
             'filename': 'general.log',
             'filters': ['require_debug_false'],
             'class': 'logging.FileHandler',
             'formatter': 'module'
         },
         'file_error': {
         	'level': 'ERROR',
         	'filename': 'errors.log',
         	'filters': ['require_debug_true'],
         	'class': 'logging.FileHandler',
         	'formatter': 'error'
         },
         'file_security': {
             'level': 'INFO',
             'filename': 'security.log',
             'filters': ['require_debug_true'],
             'class': 'logging.FileHandler',
             'formatter': 'security'
         },
         'mail_admins': {
             'level': 'ERROR',
             'class': 'django.utils.log.AdminEmailHandler'
         }
     },
     'loggers': {
         'django': {
             'handlers': ['console'],
             'propagate': True,
         },
         'django.request': {
             'handlers': ['mail_admins'],
             'level': 'ERROR',
             'propagate': False,
         },
         'django.server': {
             'handlers': ['file_error', 'mail_admins'],
         },
         'django.template': {
             'handlers': ['file_error'],
         },
         'django.db.backends': {
             'handlers': ['file_error'],
         },
         'django.security': {
             'handlers': ['file_security'],

         },

     }
 }

ALLOWED_HOSTS = []



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_apscheduler',
    'NewsPaper',
    'fpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'news.apps.NewsConfig',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'NewsPaper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATICFILES_DIRS = [
    BASE_DIR / "static"
]


LOGIN_REDIRECT_URL = "/news"

LOGOUT_REDIRECT_URL = "/news"

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

SITE_URL = 'http://127.0.0.1:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = "example@yandex.ru"


APSCHEDULER_DATETIME_FORMAT = 'N, j, Y, f:s a'

APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = ''
CELERY_RESULT_BACKEND = ''
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}