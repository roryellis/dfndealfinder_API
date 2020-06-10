from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('restaurants', views.RestaurantList.as_view(), name='restaurant_list'),
    path('restaurants/<int:pk>', views.RestaurantDetail.as_view(),
         name='restaurant_detail'),
    path('specials', views.SpecialList.as_view(), name='special_list'),
    path('specials/<int:pk>', views.SpecialDetail.as_view(),
         name='special_detail'),
]
