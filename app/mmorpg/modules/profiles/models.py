from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    email = models.EmailField(blank=False, unique=True)
    phone = models.CharField(max_length=12, blank=True, unique=True)
    bio = models.TextField(blank=True)


