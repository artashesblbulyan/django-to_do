from user.models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone


def create_profile(instance, created, sender,  **kwargs):
    if created:
        Profile.objects.create(user=instance, date_birth=timezone.now())


post_save.connect(receiver=create_profile, sender=User)
