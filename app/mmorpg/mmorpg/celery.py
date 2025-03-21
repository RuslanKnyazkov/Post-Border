import  os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mmorpg.settings')

app = Celery('mmorpg')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'delete-old-records-every-60-seconds': {
        'task': 'modules.signin.tasks.delete_old_one_time_code',
        'schedule': 60.0,
    },
}