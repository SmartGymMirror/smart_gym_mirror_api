"""
Django settings for autentificacion project.

Generated by 'django-admin startproject' using Django 5.0.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-m5uso8g+=-sntpxma19e*5h^=7^94#6uir1+%frrz0(!bo$9c5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'rest_framework',
    'djoser',
    'cuentas',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "autentificacion.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR,'build')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "autentificacion.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'auth_system',
        'USER': 'postgres',
        'PASSWORD': 'Lunalba58',
        'HOST': 'localhost',
    }
}


EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend' #para que nos envie un correo electronico
EMAIL_HOST='smtp.gmail.com' #servidor de correo
EMAIL_PORT=587 #puerto de correo
EMAIL_HOST_USER= 'albabr08@gmail.com' #correo electronico
EMAIL_HOST_PASSWORD='espejo123' #contraseña del correo electronico
EMAIL_USE_TLS=True #protocolo de seguridad

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,'build/static')
] #para que nos reconozca los archivos estaticos

STATIC_ROOT=os.path.join(BASE_DIR,'static') #para que nos guarde los archivos estaticos

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK={
    'DEFAULT_AUTHENTIFICATION_CLASSES':(
        'rest_framework.authentication.TokenAuthentication',
    ),
}

SIMPLE_JWT={
    'AUTH_HEADER_TYPES':('JWT',),
}

DJOSER={
    'LOGIN_FIELD':'email', #para que nos permita iniciar sesion con el email
    'USER_CREATE_PASSWORD_RETYPE':True, #para que nos pida confirmar la contraseña
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True, #para que nos pida confirmar el cambio de email
    'SEND_CONFIRMATION_EMAIL':True, #para que nos envie un correo de confirmacion
    'SET_USERNAME_RETYPE':True, #para que nos pida confirmar el nombre de usuario
    'SET_PASSWORD_RETYPE':True, #para que nos pida confirmar la contraseña
    'PASSWORD_RESET_CONFIRM_URL':'password/reset/confirm/{uid}/{token}', #para que nos permita cambiar la contraseña
    'USERNAME_RESET_CONFIRM_URL':'email/reset/confirm/{uid}/{token}', #para que nos permita cambiar el nombre de usuario
    'ACTIVATION_URL':'activate/{uid}/{token}', #para que nos permita activar la cuenta
    'SEND_ACTIVATION_EMAIL':True, #para que nos envie un correo de activacion
    'SERIALIZERS':{
        'user_create':'cuentas.serializers.UserCreateSerializer',
        'user':'cuentas.serializers.UserCreateSerializer',
        'user_delete':'djoser.serializers.UserDeleteSerializer',
    }
}

AUTH_USSER_MODEL='cuentas.UserAccount'
