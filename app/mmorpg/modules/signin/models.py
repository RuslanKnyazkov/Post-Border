from django.db import models
from django.contrib.auth.models import User

class OneTimeCode(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE)
    code = models.CharField(max_length=6)
    time_send = models.DateTimeField(verbose_name='Время отправки',
                                     auto_now_add=True)


