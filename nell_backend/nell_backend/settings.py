from pathlib import Path
from decouple import config
from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = []

SITE_ID = 3

# Social Auth Config
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_GITHUB_KEY = config('SOCIAL_AUTH_GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = config('SOCIAL_AUTH_GITHUB_SECRET')

SOCIAL_AUTH_DISCORD_KEY = config('SOCIAL_AUTH_DISCORD_KEY')
SOCIAL_AUTH_DISCORD_SECRET = config('SOCIAL_AUTH_DISCORD_SECRET')

SPOTIFY_CLIENT_ID = config('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = config('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = config('SPOTIFY_REDIRECT_URI')

OPENWEATHER_API_KEY = config('OPENWEATHER_API_KEY')

MICROSOFT_CLIENT_ID = config('MICROSOFT_CLIENT_ID')
MICROSOFT_CLIENT_SECRET = config('MICROSOFT_CLIENT_SECRET')
MICROSOFT_TENANT_ID = config('MICROSOFT_TENANT_ID')
MICROSOFT_REDIRECT_URI = config('MICROSOFT_REDIRECT_URI')
MICROSOFT_AUTHORITY = config('MICROSOFT_AUTHORITY')
MICROSOFT_SCOPE = config('MICROSOFT_SCOPE', cast=lambda v: [s.strip() for s in v.split(',')])

YOUTUBE_CLIENT_ID = config('YOUTUBE_CLIENT_ID')
YOUTUBE_CLIENT_SECRET = config('YOUTUBE_CLIENT_SECRET')
YOUTUBE_REDIRECT_URI = config('YOUTUBE_REDIRECT_URI')
YOUTUBE_SCOPES = config('YOUTUBE_SCOPES').split(',')

TWITCH_CLIENT_ID=config('TWITCH_CLIENT_ID')
TWITCH_CLIENT_SECRET=config('TWITCH_CLIENT_SECRET')
TWITCH_REDIRECT_URI=config('TWITCH_REDIRECT_URI')
TWITCH_SCOPES = config('TWITCH_SCOPES')

REST_USE_JWT = True

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'rest_framework',
    'rest_framework_simplejwt.token_blacklist',
    'authentication',
    'spotifys',
    'open_weather',
    'microsofts',
    'twitchs',
    'youtube',
    'drf_yasg',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.discord',
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.twitch',
    'allauth.socialaccount.providers.spotify',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'rest_framework.authtoken',
    'corsheaders',
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
    'corsheaders.middleware.CorsMiddleware',
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

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:45195",
]

CORS_ALLOW_HEADERS = [
    'content-type',
    'authorization',
    'x-csrftoken',
    'x-requested-with',
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
