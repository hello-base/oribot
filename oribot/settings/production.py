# -*- coding: utf-8 -*-
from common import *
from dj_database_url import config


# Database Settings ----------------------------------------------------------
DATABASES = {'default': config(default='postgres://localhost')}

# Sentry ---------------------------------------------------------------------
if 'SENTRY_DSN' in os.environ:
    # Add raven to the list of installed apps
    INSTALLED_APPS = INSTALLED_APPS + ['raven.contrib.django', ]
