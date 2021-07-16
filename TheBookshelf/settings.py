"""
Django settings for TheBookshelf project.

Generated by 'django-admin startproject' using Django 3.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import datetime
from pathlib import Path
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ADD THESE TWO LINES
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
FRONTEND_DIR = os.path.join(BASE_DIR, 'frontend')
CSRF_COOKIE_SECURE = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hu3_1d29+@zz0t^g59miaqx%1#o7#v^c8#7eupfy-n#x0y)b=x'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Set your auth user to the new user you have created
AUTH_USER_MODEL = 'user.AuthUser'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # third party
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'webpack_loader',
    'oauth2_provider',
    'social_django',
    'drf_social_oauth2',
    # customised app
    'user',
    'payment',
    'product'
]

# Authentication backends
AUTHENTICATION_BACKENDS = [
    # Google OAuth2
    'social_core.backends.google.GoogleOAuth2',
    # Facebook loging
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',

    # authentication setting
    'django.contrib.auth.backends.ModelBackend',
    'drf_social_oauth2.backends.DjangoOAuth2',
]
# stripe
STRIPE_PUB_KEY = 'pk_test_51IlivUBaL13Hgkoy4zeKPAQdCxH6Ys3d86BxwxBkWPFB0flVmb8eV46tocnKIIQA4NHGZpj0UeXQLHzJs8T2IaM800tTflYKN6 '
STRIPE_SECRET_KEY = 'sk_test_51IlivUBaL13HgkoypwU1xHXDwr0MCS5fctDtcsip78SBrXYqTyC42s0qZhRNlC8vVld51pyRwge7MIyzwK8B4Xm300XZ2uZJ9v '
STRIPE_WEBHOOK_KEY = 'whsec_R8I8dykTzlObMCNy2wla0C7WtqvTA5Nc'

# social Authentication
# Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '187272676634276'
SOCIAL_AUTH_FACEBOOK_SECRET = '406d68e8f9d94582cb57b03a045c79ee'
# Define SOCIAL_AUTH_FACEBOOK_SCOPE to get extra permissions from Facebook.
# Email is not sent by default, to get it, you must request the email permission.
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email'
}
SOCIAL_AUTH_USER_FIELDS = ['email', 'username', 'first_name', 'password']
# Google
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "690024386674-cpkugdn9h578rkollmjujuhj54db0v54.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "DHBUz8Jy-KqAxb_85QsHGgGqP"
# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]




# site id
SITE_ID = 1

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# corsheader whitelist
CORS_ORIGIN_WHITELIST = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True  # allow cookie

# rest framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'drf_social_oauth2.authentication.SocialAuthentication',
    ),
    # 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}


ROOT_URLCONF = 'TheBookshelf.urls'

# templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'TheBookshelf.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "assets"),
    os.path.join(BASE_DIR, "frontend/dist"),
]

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'frontend', 'webpack-stats.json')
    }
}

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
