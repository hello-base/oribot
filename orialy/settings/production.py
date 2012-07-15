# -*- coding: utf-8 -*-
from common import *
from dj_database_url import config

DATABASES = {'default': config(default='postgres://localhost')}
