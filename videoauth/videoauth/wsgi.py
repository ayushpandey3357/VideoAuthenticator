"""
WSGI config for videoauth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videoauth.settings')

application = get_wsgi_application()

# Run database migrations automatically when Gunicorn boots up on Render
try:
    from django.core.management import call_command
    call_command('migrate', interactive=False)
except Exception as e:
    print(f"Auto-migration notice on WSGI boot: {e}")

