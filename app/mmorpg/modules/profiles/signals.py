from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender = User)
def create_profile_after_registration(sender, created, instance, **kwargs):
    if created:
        UserProfile.objects.create(user = instance,
                                   email = instance.email)