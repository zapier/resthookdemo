LOCAL_SETTINGS = True
import os
from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'demo.sqlite3',                      # Or path to database file if using sqlite3.
    }
}
