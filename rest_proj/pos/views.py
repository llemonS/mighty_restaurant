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


class OrderCreateView(CreateView):
    model = OrderItem
    fields = ("food_item", "notes")

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.ticket = Ticket.objects.get(id=self.kwargs["pk"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('ticket_detail_view', args=[int(self.kwargs["pk"])])

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

    def get_queryset(self):
        var = super(TicketListView, self).get_queryset()
        return var.filter(created_by=self.request.user)


class TicketDetailView(DetailView):
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = OrderItem.objects.filter(ticket=self.kwargs['pk'])
        return context

class TicketUpdateView(UpdateView):
    model = Ticket
    fields = ("is_placed","is_completed","is_paid")

    def form_valid(self, form):
        instance = form.save(commit=False)
        if self.request.user.profile.is_server:
            instance.is_placed = True
        if self.request.user.profile.is_cook:
            instance.is_placed = True
            instance.is_completed = True
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.profile.is_server:
            return reverse('ticket_list_view', args=[int(self.kwargs["pk"])])
        if self.request.user.profile.is_cook:
            return reverse('cook_view')




class CookListView(ListView):

    model = Ticket
    template_name = 'cook.html'

    def get_queryset(self):
        var = super(CookListView, self).get_queryset()
        return var.filter(is_placed=True, is_completed=False)
