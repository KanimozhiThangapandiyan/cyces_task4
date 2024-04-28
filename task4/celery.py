import os
from celery import Celery

# Set the default broker URL
broker_url = os.environ.get('CELERY_BROKER_URL', 'redis://localhost:6379')

# Create the Celery app instance
app = Celery('task4')

# Configure app settings
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start()

