from django.conf.urls import url, include
from django.contrib import admin
from pos.views import IndexView, UserCreateView, ProfileUpdateView, FoodCreateView, FoodUpdateView, \
                      FoodDeleteView, ServerListView, OrderCreateView, TicketCreateView, \
                      TicketListView, TicketDetailView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name="profile_update_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^create_food/$', FoodCreateView.as_view(), name="food_create_view"),
    url(r'^food_item/(?P<pk>\d+)/update/$', FoodUpdateView.as_view(), name="food_update_view"),
    url(r'^food_item/(?P<pk>\d+)/delete/$', FoodDeleteView.as_view(), name="food_delete_view"),
    url(r'^server_portal/$', TicketListView.as_view(), name="ticket_list_view" ),
    url(r'^create_order/$', OrderCreateView.as_view(), name="order_create_view"),
    url(r'^create_ticket/$', TicketCreateView.as_view(), name="ticket_create_view"),
    url(r'^server_portal/(?P<pk>\d+)/$', TicketDetailView.as_view(), name="ticket_detail_view"),

]
