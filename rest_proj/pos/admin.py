from django.contrib import admin
from pos.models import Profile, FoodItem, Order

admin.site.register([Profile, FoodItem, Order])
