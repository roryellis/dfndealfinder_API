from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('restaurants', views.RestaurantList.as_view(), name='restaurant_list'),
    path('restaurants/<int:pk>', views.RestaurantDetail.as_view(),
         name='restaurant_detail'),
    # path('diningtype', views.DiningTypeList.as_view(), name='diningtype-list'),
    # path('diningtype/<int:pk>', views.DiningTypeDetail.as_view(),
    #      name='diningtype-detail'),
    # path('cuisinetype', views.CuisineTypeList.as_view(), name='cuisinetype-list'),
    # path('cuisinetype/<int:pk>', views.CuisineTypeDetail.as_view(),
    #      name='cuisinetype-detail'),
    path('specials', views.SpecialList.as_view(), name='special_list'),
    path('specials/<int:pk>', views.SpecialDetail.as_view(),
         name='special_detail'),
]
