"""
WSGI config for pmem project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
# coding=UTF-8
import os
import sys
#sys.path.append('/srv/www')
path ='/srv/www/pmem'
if path not in sys.path:sys.path.append(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pmem.settings")
os.environ.setdefault("PYTHON_EGG_CACHE", "/tmp/.python-eggs")
#os.environ['DJANGO_SETTINGS_MODULE'] = 'pmem.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
#from pmem.wsgi import PmemApplication
#application = PmemApplication(application)
