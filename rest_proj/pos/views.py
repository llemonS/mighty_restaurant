from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from pos.models import Profile, FoodItem, OrderItem, Ticket

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

class FoodCreateView(CreateView):
    model = FoodItem
    success_url = reverse_lazy('index_view')
    fields = ("title","description","price")

class FoodUpdateView(UpdateView):
    model = FoodItem
    fields = ("title","description","price")
    success_url = reverse_lazy('index_view')

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return FoodItem.objects.all()

class FoodDeleteView(DeleteView):
    model = FoodItem
    success_url = reverse_lazy('index_view')

    def get_queryset(self):
        if self.request.user.profile.is_owner:
            return FoodItem.objects.all()

class ServerListView(ListView):
    model = OrderItem
    template_name = "server.html"

# this is not being used @ the moment
class OrderCreateView(CreateView):
    model = OrderItem
    success_url = reverse_lazy('server_list_view')
    fields = ("food_item", "notes")

class TicketCreateView(CreateView):
    model = Ticket
    success_url = reverse_lazy("ticket_list_view")
    fields = ("id",)

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.created_by = self.request.user
        return super().form_valid(form)

class TicketListView(ListView):
    model = Ticket
    template_name = "server.html"

class TicketDetailView(DetailView):
    model = Ticket
