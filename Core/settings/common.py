import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'u(w1xp^p^!svu5bd4as$lbla#1g0sz57vzx3wv@grdw0u8dp_9')

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'Apps.Web.Website',
]

ROOT_URLCONF = 'Core.urls'

WSGI_APPLICATION = 'Core.wsgi.application'
