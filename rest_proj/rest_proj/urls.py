from django.conf.urls import url, include
from django.contrib import admin
from pos.views import IndexView, UserCreateView, ProfileUpdateView, FoodUpdateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name="profile_update_view"),
    url(r'^create_user$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^food_item/(?P<pk>\d+)/update/$', FoodUpdateView.as_view(), name="food_update_view"),
    #url(r'^special/(?P<pk>\d+)/delete/$', SpecialDeleteView.as_view(), name="special_delete_view"),
]
