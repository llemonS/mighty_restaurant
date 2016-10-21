from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from pos.models import Profile, FoodItem, Order

class IndexView(ListView):
    template_name = "index.html"
    model = FoodItem

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("index_view")

class ProfileUpdateView(UpdateView):
    template_name = "profile.html"
    fields = ("access_level",)
    success_url = reverse_lazy('profile_update_view')

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class FoodUpdateView(UpdateView):
    model = FoodItem
    fields = ("title","description","price")
    success_url = reverse_lazy('index_view')

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return FoodItem.objects.all()
