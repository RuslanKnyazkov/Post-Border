from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Reaction, Post, User
from django.core.mail import EmailMessage


@receiver(post_save, sender=Reaction)
def send_notification_after_created_reaction(sender, created,
                                             instance, **kwargs):
    if created:
        user = User.objects.get(
            id=instance.post_id.user.id
        )
        exsample = EmailMessage(subject='Board Post Servise',
                                body=f'На вашу публикацию был создан отклик '
                                     f'пользователем {instance.user}.',
                                to=[f'{user.email}'])
        exsample.send()
    else:
        print('Реакция измененна')
