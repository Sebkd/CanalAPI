"""
Тонкая настройка Celery
"""
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'canalapi.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
