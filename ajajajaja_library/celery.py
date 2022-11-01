import os
from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ajajajaja_library.settings')

app = Celery('ajajajaja_library')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# celery spam_tasks
app.conf.beat_schedule = {
    'send-spam-every-5-minutes': {
        'task': 'ajajajaja_library.tasks.send_spam_email',
        'schedule': crontab(minute='*/5')
    }
}