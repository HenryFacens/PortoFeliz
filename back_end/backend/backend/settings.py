from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_FRONTEND_DIR = BASE_DIR.parent.parent / 'front_end'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8_7+2o%a(-+17801qia1142#(*d%tee0@jo&5yv%5)hz7#xvq='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom apps
    'api',
    'frontend',

    # Third-party apps
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'drf_yasg',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_FRONTEND_DIR],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    # Título do site que aparece na aba do navegador
    "site_title": "Cidadania Trasnparente",

    # Título do cabeçalho do site
    "site_header": "Cidadania Trasnparente",

    # Marca do site que aparece na barra lateral
    "site_brand": "Cidadania Trasnparente",

    # Slogan de boas-vindas na página de login
    "welcome_sign": "Bem-vindo ao Portal de Cidadania Transparência",

    # Direitos autorais que aparecem no rodapé
    "copyright": "Presturion Solutions",

    # Modelo de busca padrão usado no painel admin
    "search_model": "auth.User",

    # Campo do modelo de usuário para exibir avatar
    "user_avatar": None,

    # URL do logo do site (caminho para o arquivo logo)
    # "site_logo": "core/images/logo.png",

    # URL do ícone do site (favicon)
    # "site_icon": "core/images/favicon.ico",

    # Texto do menu no canto superior direito
    # "topmenu_links": [
    #     {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
    #     {"name": "Support", "url": "https://support.example.com", "new_window": True},
    # ],

    # Links rápidos exibidos no dashboard
    # "usermenu_links": [
    #     {"name": "Support", "url": "https://support.example.com", "new_window": True},
    #     {"model": "auth.user"},
    # ],

    # Mostrar construtor de interface de usuário
    "show_ui_builder": True,

    # Ícone de um modelo (exemplo: auth)
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },

    # Modelo de menu (link, URL, permissões)
    # "nav_links": [
    #     {"name": "Documentation", "url": "https://docs.example.com", "permissions": ["auth.view_user"]},
    # ],

    # Tweaks de interface de usuário
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "core"],
    "custom_links": {
        "auth": [
            {"name": "Make Messages", "url": "make_messages", "icon": "fas fa-comments", "permissions": ["auth.view_user"]},
        ]
    },
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    # UI tweaks: https://django-jazzmin.readthedocs.io/ui_tweaks/
    "ui_tweaks": {
        "theme": "cyborg",
        "dark_mode_theme": None,
        "dark_mode_switch": True,
        "sidebar": "navbar-dark bg-primary",
        "navbar": "navbar-dark bg-dark",
        "brand_colour": "navbar-dark bg-primary",
        "accent": "accent-primary",
        "no_navbar_border": False,
        "navbar_fixed": True,
        "sidebar_fixed": True,
        "footer_fixed": True,
        "buttons": {
            "style": "primary",
        },
        "body_small_text": False,
        "navbar_small_text": False,
        "sidebar_small_text": False,
        "footer_small_text": False,
    },
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=50),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',

    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

CORS_ALLOW_ALL_ORIGINS = True
