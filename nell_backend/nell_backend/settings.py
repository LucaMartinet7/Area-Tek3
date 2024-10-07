from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.spotify',
    'rest_framework',
    'drf_yasg',
    'authentication',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'nell_backend.urls'

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

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 3
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'nell_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY'),
            'secret': os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET'),
            'key': ''
        }
    },
    'github': {
        'APP': {
            'client_id': os.getenv('SOCIAL_AUTH_GITHUB_KEY'),
            'secret': os.getenv('SOCIAL_AUTH_GITHUB_SECRET'),
            'key': ''
        }
    },
    'discord': {
        'APP': {
            'client_id': os.getenv('SOCIAL_AUTH_DISCORD_KEY'),
            'secret': os.getenv('SOCIAL_AUTH_DISCORD_SECRET'),
            'key': ''
        }
    },
    'microsoft': {
        'APP': {
            'client_id': os.getenv('MICROSOFT_CLIENT_ID'),
            'secret': os.getenv('MICROSOFT_CLIENT_SECRET'),
            'key': ''
        }
    },
    'youtube': {
        'APP': {
            'client_id': os.getenv('YOUTUBE_CLIENT_ID'),
            'secret': os.getenv('YOUTUBE_CLIENT_SECRET'),
            'key': ''
        }
    },
    'twitch': {
        'APP': {
            'client_id': os.getenv('TWITCH_CLIENT_ID'),
            'secret': os.getenv('TWITCH_CLIENT_SECRET'),
            'key': ''
        }
    },
    'spotify': {
        'APP': {
            'client_id': os.getenv('SPOTIFY_CLIENT_ID'),
            'secret': os.getenv('SPOTIFY_CLIENT_SECRET'),
            'key': ''
        }
    },
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
