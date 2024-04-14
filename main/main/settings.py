import os
import logging
from django.utils.log import AdminEmailHandler
from pathlib import Path

from django.urls import reverse_lazy

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'djangawewaeo-insecurawewaeq21321dqee-(we2^&=i$jywk)fbx@-5bjd*fb%fnv7(4h6*a+aaju43x&5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'modeltranslation',  # перевод обьязательно до админа

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # filters
    'django_filters',
    'django.contrib.sites',
    # apps
    'news',
    'appointment',
    'sign',

    # allauth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.google',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # mymiddleware
    'news.middlewares.TimezoneMiddleware',  # add that middleware!
    
    # allauth
    'allauth.account.middleware.AccountMiddleware',

]


AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR / 'templates')],
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

WSGI_APPLICATION = 'main.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'pricegitpostgres1',
        'HOST': 'localhost',
        'PORT': '5433',
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGE_SESSION_KEY = [
    ('en-us', 'English'),
    ('ru', 'Русский')
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# addproject - email
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'imaralievasadbek'  # ваше имя пользователя, например, если ваша почта user@yandex.ru, то сюда надо писать user, иными словами, это всё то что идёт до собаки
EMAIL_HOST_PASSWORD = 'apvuvdxxueyomifk'  # пароль от почты(а не от аккаунта)
EMAIL_USE_SSL = True  # Яндекс использует ssl, подробнее о том, что это, почитайте в дополнительных источниках, но включать его здесь обязательно


# addproject - caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT': 10,
        # Указываем, куда будем сохранять кэшируемые файлы! Не забываем создать папку cache_files внутри папки с manage.py!
    }

}


#  Регистрация по электронной почте.
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'


'''
#     Чтобы allauth распознал нашу форму как ту, 
#     что должна выполняться вместо формы по умолчанию, 
#     необходимо добавить строчку в файл настроек проекта settings.py:
# '''
# ACCOUNT_FORMS = {'signup': 'sign.models.BasicSignupForm'}

# Добавление адреса перенаправления после успешного входа в систему в файл настроек проекта (settings.py):
LOGIN_URL = 'sign/login/'
SITE_ID = 1
LOGIN_REDIRECT_URL = "news:news_list"
LOGOUT_REDIRECT_URL = "/sign/login/"

# logging


# Определяем формат сообщений
log_format = '%(asctime)s [%(levelname)s] %(pathname)s: %(message)s'
date_format = '%Y-%m-%d %H:%M:%S'

# Определяем общие настройки для всех обработчиков
common_handler_settings = {
    'level': logging.DEBUG if DEBUG else logging.INFO,
    'formatter': logging.Formatter(log_format, date_format),
}

# Определяем обработчик для консоли
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging.Formatter(log_format, date_format))
console_handler.setLevel(logging.DEBUG)  # Выводить все сообщения от уровня DEBUG

# Определяем обработчик для файла general.log
general_log_file = os.path.join(BASE_DIR, 'general.log')
general_log_handler = logging.FileHandler(general_log_file)
general_log_handler.setFormatter(logging.Formatter(log_format, date_format))
general_log_handler.setLevel(logging.INFO)  # Выводить сообщения уровня INFO и выше

# Определяем обработчик для файла errors.log
errors_log_file = os.path.join(BASE_DIR, 'errors.log')
errors_log_handler = logging.FileHandler(errors_log_file)
errors_log_handler.setFormatter(logging.Formatter(log_format, date_format))
errors_log_handler.setLevel(logging.ERROR)  # Выводить сообщения уровня ERROR и выше

# Определяем обработчик для файла security.log
security_log_file = os.path.join(BASE_DIR, 'security.log')
security_log_handler = logging.FileHandler(security_log_file)
security_log_handler.setFormatter(logging.Formatter(log_format, date_format))
security_log_handler.setLevel(logging.DEBUG)  # Выводить сообщения от уровня DEBUG и выше

# Определяем логгер для django.request и django.server
django_request_logger = logging.getLogger('django.request')
django_request_logger.addHandler(errors_log_handler)  # Ошибки попадают в errors.log
django_request_logger.setLevel(logging.ERROR)  # Выводить сообщения уровня ERROR и выше

django_server_logger = logging.getLogger('django.server')
django_server_logger.addHandler(errors_log_handler)  # Ошибки попадают в errors.log
django_server_logger.setLevel(logging.ERROR)  # Выводить сообщения уровня ERROR и выше

# Определяем логгер для django.security
django_security_logger = logging.getLogger('django.security')
django_security_logger.addHandler(security_log_handler)  # Все сообщения попадают в security.log
django_security_logger.setLevel(logging.DEBUG)  # Выводить сообщения от уровня DEBUG и выше

# Установка фильтров для обработчиков
console_handler.addFilter(lambda record: DEBUG)  # Выводить в консоль только при DEBUG = True
general_log_handler.addFilter(lambda record: not DEBUG)  # Выводить в general.log только при DEBUG = False
admin_email_handler = AdminEmailHandler()
admin_email_handler.setLevel(logging.ERROR)  # Отправлять на почту сообщения уровня ERROR и выше

# Добавляем обработчики к логгеру по умолчанию
root_logger = logging.getLogger('')
root_logger.setLevel(logging.DEBUG)  # Включаем все сообщения для корневого логгера
root_logger.addHandler(console_handler)
root_logger.addHandler(general_log_handler)

# Добавляем обработчик почтовых сообщений к логгеру django.request
django_request_logger.addHandler(admin_email_handler)




