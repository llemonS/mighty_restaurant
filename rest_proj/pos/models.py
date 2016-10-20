from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

ACCESS_LEVELS = [
    ("s", "Server"),
    ("c", "Cook"),
    ("o", "Owner")
]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)

@receiver(post_save, sender='auth.user')
def create_profile(sender, **kwargs):
    instance = kwargs["instance"]
    created = kwargs["created"]
    if created:
        Profile.objects.create(user=instance)
