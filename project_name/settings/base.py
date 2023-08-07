from os import getenv as os_getenv, path as os_path  # noqa
from pathlib import Path

from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = get_random_secret_key()

DEBUG = True

ALLOWED_HOSTS =['app.backend.dev','127.0.0.1','.vercel.app']   # os_getenv("ALLOWED_HOSTS", "localhost").split(",")


# if DEBUG:
#     CORS_ORIGIN_ALLOW_ALL = True
# else:
#     CSRF_TRUSTED_ORIGINS = os_getenv("CSRF_TRUSTED_ORIGINS", "http://localhost").split(
#         ","
#     )
#     CORS_ALLOWED_ORIGINS = os_getenv("CORS_ALLOWED_ORIGINS", "http://localhost").split(
#         ","
#     )

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "test_app",
    "forum",
    "authapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # CorsMiddleware should be placed as high as possible,
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project_name.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "project_name.wsgi.app"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os_path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os_getenv("POSTGRES_DATABASE", "verceldb"),
        "USER": os_getenv("POSTGRES_USER", "default"),
        "PASSWORD": os_getenv("POSTGRES_PASSWORD", "password"),
        "HOST": os_getenv("POSTGRES_HOST", "ep-curly-glade-57879119.us-east-1.postgres.vercel-storage.com"),
        "PORT": os_getenv("POSTGRES_PORT", "5432"),
        'OPTIONS': {'sslmode': 'require'},
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os_path.join(BASE_DIR, "static")
MEDIA_URL = "media/"
MEDIA_ROOT = os_path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"




#login
LOGIN_URL = '/authapp/signin'
