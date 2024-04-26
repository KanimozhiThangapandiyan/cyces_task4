
# celery.py

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task4.settings')

app = Celery('task4')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
