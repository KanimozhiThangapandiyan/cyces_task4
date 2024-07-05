from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task4.settings')

app = Celery('task4')

# Configure Celery using settings from Django settings.py.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = {
    'postman_queue': {
        'exchange': 'postman',
        'routing_key': 'postman',
    },
    'periodic_queue': {
        'exchange': 'periodic',
        'routing_key': 'periodic',
    },
    'bulk_upload_queue': {
        'exchange': 'bulk_upload',
        'routing_key': 'bulk_upload',
    },
}

# Load tasks from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.broker_connection_retry_on_startup = True

# Configure Celery Beat scheduler
app.conf.beat_schedule = {
    'run_summaa_weekly': {
        'task': 'apps.cms.tasks.summaa',
        # 'schedule': crontab(day_of_week=6, hour=23, minute=59),  #at 23:59 (11:59 PM) every Saturday
        'schedule': crontab(minute='*/5'),
    },
}