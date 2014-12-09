"""
Django settings for pmem project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# -*- coding:utf-8 -*-
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!8)lj7(8n%gw2rhow*i#ghgq@h$he(!ngr*+t(0uf2+xvft&-('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = (
os.path.join(BASE_DIR, 'templates').replace('\\','/'),
)
ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'mytrip',
	'south',
	'social_auth',
	'django_facebook',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
)

ROOT_URLCONF = 'pmem.urls'

WSGI_APPLICATION = 'pmem.wsgi.application'

AUTHENTICATION_BACKENDS =(
	'social_auth.backends.facebook.FacebookBackend',
	'django_facebook.auth_backends.FacebookBackend',
	'django.contrib.auth.backends.ModelBackend',
)
FACEBOOK_APP_ID = '4637XXXXXXXXXXXXXXXX'
FACEBOOK_API_SECRET = 'XXXXXXXXXXXXXXXXX'
FACEBOOK_EXTENDED_PERMISSIONS = ['email']
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/another-login-url/'
#LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'
SOCIAL_AUTH_LOGIN_URL = '/login-url/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/login-error/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/new-users-redirect-url/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/new-association-redirect-url/'
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'
#AUTH_USER_MODEL = "mytrip.User"
AUTH_PROFILE_MODULE= 'mytrip.User'
LOGIN_URL = '/login-form/'
LOGOUT_URL = '/mytrip/logout/'
#Django facebook
TEMPLATE_CONTEXT_PROCESSORS=(
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.tz',
	'django.core.context_processors.request',
	'django.contrib.messages.context_processors.messages',
	'django_facebook.context_processors.facebook',
)
# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        #'NAME': 'django_db',
	#'USER': 'daven',
	#'PASSWORD':'',
	'HOST': '',
	'PORT': '',
	'OPTIONS':{
		'read_default_file':'/etc/mysql/my.cnf',
	},
    }
}
ROOT ='/srv/www/pmem' #new add
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'zh-TW'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

#USE_TZ = True
#Auto set timezone when datetime added
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT =os.path.join(BASE_DIR,'static').replace('\\','/')# "/srv/www/pmem/static/" os.path.join(BASE_DIR,'pmem/static')
STATICFILES_DIRS = (
	os.path.join(BASE_DIR,'mytrip/static/').replace('\\','/'),
   # "/srv/www/pmem/static/mytrip",
)

ADMIN_MEDIA_ROOT='static/admin'
MEDIA_ROOT = os.path.join(BASE_DIR,'media').replace('\\', '/')
STATIC_PATH='/srv/www/pmem/static/'
MEDIA_PATH='/srv/www/pmem/media/'
#CSRF_COOKIE_SECURE = True

#CSRF_COOKIE_NAME = 'csrfmiddlewaretoken'
SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    #'social_auth.backends.pipeline.misc.save_status_to_session',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'mytrip.pipeline.create_profile',
    'mytrip.pipeline.set_guardian_permissions',
    )
