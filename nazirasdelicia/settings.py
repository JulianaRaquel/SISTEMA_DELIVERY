import os
from pathlib import Path
from django.contrib.messages import constants
from decouple import config, Csv
from dj_database_url import parse as db_url

# Diretório base
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave Secreta
SECRET_KEY = config('SECRET_KEY')

# Variável DEBUG
DEBUG = config('DEBUG', cast=bool, default=False)

# Hosts Permitidos
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Aplicações do Projeto

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'produto',
    'pedido',
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

ROOT_URLCONF = 'nazirasdelicia.urls'

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
            ],
        'libraries':{
            'filtros': 'produto.templatestags.filtros',

            }
        },
    },
]

WSGI_APPLICATION = 'nazirasdelicia.wsgi.application'


# Banco de Dados

# Banco de Dados

DATABASES = {
    'default': config(
        'DATABASE_URL',
        default='sqlite:///' + str(BASE_DIR / 'db.sqlite3'),
        cast=db_url
    )
}

# Validação de Senhas

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


# Região e Fuso Horário

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'


# Arquivos Estáticos (CSS, JavaScript, Images)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Arquivos de Upload

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SESSION_COOKIE_AGE = 60*60*24*7

SESSION_SAVE_EVERY_REQUEST = False

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Messages

MESSAGE_TAGS = {
    constants.DEBUG: 'alert-primary',
    constants.ERROR: 'alert-danger',
    constants.SUCCESS: 'alert-SUCCESS',
    constants.INFO: 'alert-info',
    constants.WARNING: 'alert-warning',
}

#CSRF_TRUSTED_ORIGINS = ["https://delivery-system.fly.dev"]
