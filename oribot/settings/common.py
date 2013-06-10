# -*- coding: utf-8 -*-
from os.path import abspath, basename, dirname, join, normpath
from sys import path


# Path Configuration =========================================================
DJANGO_ROOT = dirname(dirname(abspath(__file__)))
SITE_ROOT = dirname(DJANGO_ROOT)
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our
# project name in our dotted import paths:
path.append(DJANGO_ROOT)

# Default / Debug Settings ---------------------------------------------------
DEBUG = True
TEMPLATE_DEBUG = DEBUG
ROOT_URLCONF = '%s.urls' % SITE_NAME
SITE_ID = 1

# Emails ---------------------------------------------------------------------
ADMINS = [('Bryan Veloso', 'bryan@hello-ranking.com')]
MANAGERS = [('Jennifer Verduzco', 'jen@hello-ranking.com')]

# Localization Settings ------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Template Settings ----------------------------------------------------------
TEMPLATE_DIRS = (normpath(join(DJANGO_ROOT, 'templates')),)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# Installed Applications -----------------------------------------------------
DJANGO_APPLICATIONS = [
    'django.contrib.contenttypes',
    'django.contrib.humanize',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
COMPONENTS = [
]
PLUGINS = [
]
ADMINISTRATION = [
    'django.contrib.admin',
]
INSTALLED_APPS = DJANGO_APPLICATIONS + COMPONENTS + PLUGINS + ADMINISTRATION


# Asset Serving ==============================================================
# Media Settings -------------------------------------------------------------
MEDIA_ROOT = normpath(join(DJANGO_ROOT, 'media'))
MEDIA_URL = '/media/'

# Static Media Settings ------------------------------------------------------
STATIC_ROOT = normpath(join(DJANGO_ROOT, 'static'))
STATIC_URL = '/static/'
STATICFILES_DIRS = (normpath(join(DJANGO_ROOT, 'assets')),)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
