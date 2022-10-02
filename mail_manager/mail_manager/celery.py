import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mail_manager.settings")

app = Celery("mail_manager")
app.conf.timezone = 'UTC'

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'add-every-30-seconds': {
    #     'task': 'unity.tasks.add30s',
    #     'schedule': 30.0,
    #     'args': (16, 16)
    # },
    'show-new-email-add-in-current-month': {
        'task': 'unity.tasks.newMailInCurrentMonth',
        'schedule': crontab(hour=7, minute=30, day_of_week='1,3'),
    }
}