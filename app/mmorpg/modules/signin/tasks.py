from celery import shared_task
from django.utils import timezone
from .models import OneTimeCode
@shared_task
def delete_old_one_time_code():
    test = OneTimeCode.objects.filter(
        time_send__gt = timezone.now() - timezone.timedelta(seconds=60)).delete()



