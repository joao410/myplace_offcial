"""
Django settings for back_help project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7g)498955!1d-$f=0v#9t0%*v%tu5#d=#$it0mbmm6b$c)0)ow'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    

    'helpdesk',
    'users',
    'login',
    'performance',
    'inventory',
    'files',
    
    
    
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

ROOT_URLCONF = 'back_help.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'back_help.wsgi.application'
# DATABASE_ROUTERS = [ 
#     'helpdesk.dbrouters.ChamadosDBRouter',
#     'performance.dbrouters.PerformanceDBRouter',
#     'inventory.dbrouters.InventoryDBRouter',
#     'purchases.dbrouters.PurchasesDBRouter',
#                         ]


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'SY_RH',
        'USER': 'tigenios',
        'PASSWORD': '0567senh@',
        'HOST': 'tigenios',
        'PORT': '1433',

        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    },
    # 'online':{
    #     'ENGINE': 'sql_server.pyodbc',
    #     'NAME': 'Online',
    #     'USER': 'tigenios',
    #     'PASSWORD': '0567senh@',
    #     'HOST': 'tigenios',
    #     'PORT': '1433',

    #     'OPTIONS': {
    #         'driver': 'ODBC Driver 17 for SQL Server',
    #     },
    # },
    # 'tickets':{
    #     'ENGINE': 'sql_server.pyodbc',
    #     'NAME': 'Tickets',
    #     'USER': 'tigenios',
    #     'PASSWORD': '0567senh@',
    #     'HOST': 'tigenios',
    #     'PORT': '1433',

    #     'OPTIONS': {
    #         'driver': 'ODBC Driver 17 for SQL Server',
    #     },
    # },
    # 'inventory':{
    #     'ENGINE': 'sql_server.pyodbc',
    #     'NAME': 'Inventory',
    #     'USER': 'tigenios',
    #     'PASSWORD': '0567senh@',
    #     'HOST': 'tigenios',
    #     'PORT': '1433',

    #     'OPTIONS': {
    #         'driver': 'ODBC Driver 17 for SQL Server',
    #     },
    # },
}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'HELPDESK',
#        'USER': 'arena',
#        'PASSWORD': 'arena127',
#        'HOST': 'localhost',
#        'PORT': '5432',
#        
#}    }
#}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
PREVIEW_ROOT = os.path.join(BASE_DIR, 'preview')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'back_help/static')]


