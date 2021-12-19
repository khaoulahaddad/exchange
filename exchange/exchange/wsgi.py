"""
WSGI config for exchange project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from alpha.worker import Worker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exchange.settings')

application = get_wsgi_application()
worker= Worker()
worker.run_continuously(3600)
