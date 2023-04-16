"""
Django settings for football project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",
    "predictions",
    'cloudinary',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.instagram',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'football.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'predictions.context_processors.current_site_processor',
            ],
        },
    },
]
WSGI_APPLICATION = 'football.wsgi.application'
AUTH_USER_MODEL = "predictions.User"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'URL': os.environ.get('DATABASE_URL'),
        # 'NAME': os.environ.get('DATABASE_NAME'),
        # 'USER': os.environ.get('DATABASE_USER'),
        # 'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        # 'HOST': os.environ.get('DATABASE_HOST'),
        # 'PORT': os.environ.get('DATABASE_PORT'),
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        "VERIFIED_EMAIL": True,
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'offline',
        },
        'OAUTH_PKCE_ENABLED': True,
        'APP': {
            'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
            'secret': os.environ.get("GOOGLE_CLIENT_SECRET"),
            'key': ''
        }
    },
    'instagram': {
        "VERIFIED_EMAIL": True,
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP': {
            'client_id': os.environ.get("INSTA_CLIENT_ID"),
            'secret': os.environ.get("INSTA_CLIENT_SECRET"),
            'key': ''
        }
    },
    'facebook': {
        "VERIFIED_EMAIL": True,
        'SCOPE': [
            'profile',
            'email',
        ],
        'APP': {
            'client_id': os.environ.get("FB_CLIENT_ID"),
            'secret': os.environ.get("FB_CLIENT_SECRET"),
            'key': ''
        }
    },
}

cloudinary.config( 
  cloud_name = os.environ.get('cloud_name'), 
  api_key = os.environ.get('api_key'), 
  api_secret = os.environ.get('api_secret')
)

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

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MERCHANT_ID = os.environ.get("Merchant_Id")
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL="/"
EMAIL_FROM_USER = os.environ.get('EMAIL_FROM_USER')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
RAVE_PUBLIC_KEY = os.environ.get('RAVE_PUBLIC_KEY')
RAVE_SECRET_KEY = os.environ.get("RAVE_SECRET_KEY")