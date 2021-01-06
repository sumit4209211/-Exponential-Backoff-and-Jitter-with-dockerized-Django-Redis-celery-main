
import os
import random
from celery import Celery
from celery.schedules import crontab
from celery.task import task
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'samplesite.settings')
 
app = Celery('samplesite')
app.config_from_object('django.conf:settings')
 
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'publisher.tasks.send_view_count_report',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}


@task(bind=True, autoretry_for=(Exception,), retry_backoff=5, retry_jitter=True, retry_kwargs={'max_retries': 5})
def task_process_notification(self):
    if not random.choice([0, 1]):
        # mimic random error
        raise Exception()

    requests.post('http://localhost:8000/delay/5')
    
	