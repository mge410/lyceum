import os
from pathlib import Path
from typing import List

import environ

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, 'secret_key'),
    ALLOWED_HOSTS=(list, ['*']),
    DEFAULT_USER_ACTIVITY=(bool, None),
    REVERSE_MIDDLEWARE=(bool, False),
    NUMBER_OF_LOGIN_ATTEMPTS=(int, 5),
    MAIL_SENDER=(str, 'v0v.voron2005@yandex.ru'),
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

DEFAULT_USER_ACTIVITY = env('DEFAULT_USER_ACTIVITY')

if DEFAULT_USER_ACTIVITY is None:
    DEFAULT_USER_ACTIVITY = True if DEBUG else False

ALLOWED_HOSTS: List[str] = env('ALLOWED_HOSTS')

INSTALLED_APPS = [
    # Main apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    # Other apps
    'ckeditor',
    'debug_toolbar',
    'django_cleanup.apps.CleanupConfig',
    'sorl.thumbnail',
    # Our apps
    'about.apps.AboutConfig',
    'catalog.apps.CatalogConfig',
    'core.apps.CoreConfig',
    'download.apps.DownloadConfig',
    'feedback.apps.FeedbackConfig',
    'homepage.apps.HomepageConfig',
    'rating.apps.RatingConfig',
    'users.apps.UsersConfig',
    'stats.apps.StatsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

REVERSE_MIDDLEWARE = env('REVERSE_MIDDLEWARE')

if REVERSE_MIDDLEWARE:
    MIDDLEWARE.append('lyceum.middleware.middleware.ReverseMiddleware')

INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'lyceum.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'lyceum.context_processors.birthday.birthday_people',
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
        'NAME': 'django.contrib.auth.password_validation.'
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
        'NumericPasswordValidator',
    },
]

AUTHENTICATION_BACKENDS = [
    'users.backends.AuthBackend',
]

LOGIN_URL = 'auth/login/'
LOGIN_REDIRECT_URL = '/'

LANGUAGES = (
    ('en', ('English',)),
    ('ru', ('Russian',)),
)

LANGUAGE_CODE = 'en'

LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale/')]

MAIL_SENDER = env('MAIL_SENDER')

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'

NUMBER_OF_LOGIN_ATTEMPTS = env('NUMBER_OF_LOGIN_ATTEMPTS')

EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static_dev',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'toolbar_Basic': [['Source', '-', 'Bold', 'Italic']],
        'toolbar_YourCustomToolbarConfig': [
            {
                'name': 'document',
                'items': [
                    'Source',
                ],
            },
            {
                'name': 'clipboard',
                'items': [
                    'Cut',
                    'Copy',
                    'Paste',
                    'PasteText',
                    'PasteFromWord',
                    '-',
                    'Undo',
                    'Redo',
                ],
            },
            {
                'name': 'editing',
                'items': ['Find', 'Replace', '-', 'SelectAll'],
            },
            '/',
            {
                'name': 'basicstyles',
                'items': [
                    'Bold',
                    'Italic',
                    'Underline',
                    'Strike',
                    'Subscript',
                    'Superscript',
                    '-',
                    'RemoveFormat',
                ],
            },
            {
                'name': 'paragraph',
                'items': [
                    'NumberedList',
                    'BulletedList',
                    '-',
                    'Outdent',
                    'Indent',
                    '-',
                    'Blockquote',
                    'CreateDiv',
                    '-',
                    'JustifyLeft',
                    'JustifyCenter',
                    'JustifyRight',
                    'JustifyBlock',
                    '-',
                    'BidiLtr',
                    'BidiRtl',
                    'Language',
                ],
            },
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {
                'name': 'insert',
                'items': [
                    'Flash',
                    'Table',
                    'HorizontalRule',
                    'Smiley',
                    'SpecialChar',
                    'PageBreak',
                ],
            },
            '/',
            {
                'name': 'styles',
                'items': ['Styles', 'Format', 'Font', 'FontSize'],
            },
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        ],
        'toolbar': 'YourCustomToolbarConfig',
        'tabSpaces': 4,
        'extraPlugins': ','.join(
            [
                'div',
                'autolink',
                'autoembed',
                'embedsemantic',
                'autogrow',
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'elementspath',
            ]
        ),
    }
}
