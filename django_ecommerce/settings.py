import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# media for images
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# TODO: DEBUG = False, change host, move secret_key to a different file + generate a new key for production: https://humberto.io/blog/tldr-generate-django-secret-key/

with open('django_ecommerce/key.txt', 'r') as fp:
    SECRET_KEY = fp.read().strip()

DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

# two apps, one for login and another for the shop
# + 2 modules; crispy forms and the recaptcha with register
INSTALLED_APPS = [
    # installs
    'django_countries',
    'captcha',
    'crispy_forms',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # apps
    'login',
    'shop',
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

ROOT_URLCONF = 'django_ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),], # template is in main project folder and not in each individual app folder
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

WSGI_APPLICATION = 'django_ecommerce.wsgi.application'


# Database => SQLite
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST':'localhost',
#         'PORT':''
        

#     }
# }



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'

# static files also in the main project directory
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# login url and its redirect
LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

# added crispy module for forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# recaptcha keys, generate a new one here-> https://www.google.com/recaptcha/admin/create (note, v2)
RECAPTCHA_PUBLIC_KEY = '6LftJ6wZAAAAANJrMfgEZ2K-AkHkUbR_-4Bm12f2'

RECAPTCHA_PRIVATE_KEY = '6LftJ6wZAAAAAMGGD891Cd6CWjT7N4xJFYnJ5NhG'

#STRIPE_SECRET_KEY =  "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
STRIPE_SECRET_KEY =  "sk_test_51LooCOE5APAQstyh9hI3K2BOgR6oVJKZIyXcPMkF9Hpc7nbtZIY37MELO7FCoMdZKA3rpL4xocQfogVedgIdduRD00wuZoLMlx"

# debug email server, run with => python -m smtpd -n -c DebuggingServer localhost:1025
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
