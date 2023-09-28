from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g&x(2l9(ywi7hz#1j1@^3g(=)*8h(ntbc^sbo$o(_r@s8=%e4#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'harmeet_singh1@softprodigy.com'  # Your Gmail email address
EMAIL_HOST_PASSWORD = 'sdfl gcin kvrt ited' 



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'serializers_app',
    'stripe_payment',
    'rayzorpay_payment',
    'custom_commands',
    'signals',
    'celery',
    'celery_app',
    'django_celery_beat',
]
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 2,  # Number of items per page
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


CELERY_BROKER_URL = 'redis://localhost:6379/0'
  
# set the celery result backend
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
  
# set the celery timezone
CELERY_TIMEZONE = 'UTC'

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels_redis.core.RedisChannelLayer",
        "CONFIG": {
            "hosts": [("localhost", 6379)],
        },
    },
}


STRIPE_PUBLISHABLE_KEY = 'pk_test_51Mg4qcSHH6lTciJepNZxG7YQJvNYcnXm58AXGOrt3hzfyPaxofrhn3LvVBfTzFmkgTh9DPG8AaHEzmjeNQ65FaCM00v5XlKKXf'
STRIPE_SECRET_KEY = 'sk_test_51Mg4qcSHH6lTciJeaGNI4OHXueQleXieDaBKw4dQoPQWNBQMFOsplYfSTBVwdBStSJQLlFvFPphfFvIKUy3wAyyn008SW57vtP'


RAZOR_KEY_ID = 'rzp_test_2tFW5rskhl54YT'
RAZOR_KEY_SECRET = 'JHjMTXuiXWs7rQWN8vvQ8Ko7'

# STATIC_URL = '/static/'

# for django >= 3.1
STATICFILES_DIRS = [BASE_DIR / 'static']



APPEND_SLASH=False


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'serializers_practice.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
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

WSGI_APPLICATION = 'serializers_practice.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Serializers',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
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
