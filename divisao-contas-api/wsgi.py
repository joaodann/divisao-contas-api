"""
WSGI config for divisao-contas-api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "divisao-contas-api.config")

import configurations
configurations.setup()

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
