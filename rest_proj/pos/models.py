from django.db import models

ACCESS_LEVELS = [
    ("s", "Server"),
    ("c", "Cook"),
    ("o", "Owner")
]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    access_level = models.CharField(max_length=1, choices=ACCESS_LEVELS)
