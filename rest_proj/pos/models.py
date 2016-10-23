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

    @property
    def is_owner(self):
        return self.access_level == 'o'
    @property
    def is_server(self):
        return self.access_level == 'c'
    @property
    def is_server(self):
        return self.access_level == 's'

@receiver(post_save, sender='auth.user')
def create_profile(sender, **kwargs):
    instance = kwargs["instance"]
    created = kwargs["created"]
    if created:
        Profile.objects.create(user=instance)

class FoodItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.title

class Ticket(models.Model):
    created_by = models.ForeignKey('auth.user')
    created_time = models.DateTimeField(auto_now_add=True)
    is_placed = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    food_item = models.ForeignKey(FoodItem)
    ticket = models.ForeignKey(Ticket)
    notes = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.food_item)
