from django.contrib import admin
from pos.models import Profile, FoodItem, OrderItem, Ticket

admin.site.register([Profile, FoodItem, OrderItem, Ticket])
