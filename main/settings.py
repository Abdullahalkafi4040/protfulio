from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Security
SECRET_KEY = 'django-insecure-your-automatically-generated-secret-key-string'

# Production-e False hobe (local testing-er shomoy True rakhte paren)
DEBUG = False

ALLOWED_HOSTS = ['*']

# Application definition (Database-free portfolio-r jonno lightweighted kora holo)
INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "baseapp",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "main.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
            ],
        },
    },
]

WSGI_APPLICATION = "main.wsgi.application"

# Database bad dewa holo karon Vercel-e SQLite kaj kore na (read-only filesystem)
DATABASES = {}

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = []
BASE_STATIC_DIR = BASE_DIR / "base" / "static"

if BASE_STATIC_DIR.is_dir():
    STATICFILES_DIRS.append(BASE_STATIC_DIR)

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"