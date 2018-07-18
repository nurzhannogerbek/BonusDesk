import os
from celery.schedules import crontab
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '...'

DEBUG = True

ALLOWED_HOSTS = [
    '*'
]

INSTALLED_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',  # django-widget-tweaks
    'account',  # django-user-accounts
    'pinax.referrals',  # pinax-referrals
    'mptt',  # django-mptt
    'bootstrap_datepicker_plus',  # django-bootstrap-datepicker-plus
    'phonenumber_field',  # django-phonenumber-field
    'dashboard',  # 'dashboard' application
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

ROOT_URLCONF = 'BonusDesk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'BonusDesk.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '...',
        'USER': '...',
        'PASSWORD': '...',
        'HOST': '...',
        'PORT': '...',
    }
}

# Password validation
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

# The ID, as an integer, of the current site in the django_site database table
SITE_ID = 1

# START: Internationalization
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True
# END: Internationalization

# The absolute path to the directory where static files (CSS, JavaScript, Images) located
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# URL to use when referring to static files located in STATIC_ROOT
STATIC_URL = '/static/'

# The absolute path to the directory where collectstatic command will collect static files for deployment
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

EMAIL_HOST = '...'
EMAIL_PORT = '...'
EMAIL_HOST_USER = '...'
EMAIL_HOST_PASSWORD = '...'
EMAIL_USE_TLS = '...'
SERVER_EMAIL = '...'

# START: CELERY settings
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Almaty'
CELERY_BEAT_SCHEDULE = {
    "amount-counting": {
        "task": "dashboard.tasks.amount_counting",
        "schedule": crontab(0, 0, day_of_month=1),
    },
}
# END: CELERY settings

# START: Bonus System
PRICE = os.environ.get('PRICE')
CLASSIC = os.environ.get('CLASSIC') or '150000'
SILVER = os.environ.get('SILVER') or '300000'
SILVER_BONUS = os.environ.get('SILVER_BONUS') or '75000'
GOLD = os.environ.get('GOLD') or '600000'
GOLD_BONUS = os.environ.get('GOLD_BONUS') or '300000'
PLATINUM = os.environ.get('PLATINUM') or '1200000'
PLATINUM_BONUS = os.environ.get('PLATINUM_BONUS') or '1200000'
BRILLIANT = os.environ.get('BRILLIANT') or '2400000'
BRILLIANT_BONUS = os.environ.get('BRILLIANT_BONUS') or '3600000'
# END: Bonus System

# START: Logging settings
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(asctime)s] | %(levelname)s | %(message)s',
            'datefmt': '%d/%b/%Y %H:%M:%S',
        },
    },
    'handlers': {
        'debug': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logging/debug.log',
            'maxBytes': 1024*1024*5,
            'formatter': 'simple',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logging/error.log',
            'maxBytes': 1024*1024*5,
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
            'handlers': ['debug', 'error'],
        },
    },
}
# END: Logging settings

ACCOUNT_EMAIL_CONFIRMATION_EMAIL = False
ACCOUNT_SIGNUP_REDIRECT_URL = '/dashboard/'
LOGIN_URL = reverse_lazy('account_login')
LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGOUT_REDIRECT_URL = reverse_lazy('account_login')
