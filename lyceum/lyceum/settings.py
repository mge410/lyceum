from pathlib import Path

import environ

env = environ.Env(
    DEBUG=(str, 'True'),
    SECRET_KEY=(str, 'secret_key'),
    ALLOWED_HOSTS=(list, ['*']),
    REVERSE_MIDDLEWARE=(str, 'true'),
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')

DEBUG = str(env('DEBUG')).lower() in ['true', '1', 'y', 'yes']

ALLOWED_HOSTS: list[str] = env('ALLOWED_HOSTS')

INSTALLED_APPS = [
    # Main apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    # Other apps
    'debug_toolbar',
    # Our apps
    'about.apps.AboutConfig',
    'catalog.apps.CatalogConfig',
    'homepage.apps.HomepageConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

REVERSE_MIDDLEWARE = str(env('REVERSE_MIDDLEWARE')).lower() in ['true', '1', 'y', 'yes']

if REVERSE_MIDDLEWARE:
    MIDDLEWARE.append('lyceum.middleware.middleware.ReverseMiddleware')

INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'lyceum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'lyceum.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' 'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' 'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' 'NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
