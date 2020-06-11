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
    path('cuisinetypes', views.CuisineTypeList.as_view(), name='cuisinetype_list'),
    path('diningtypes', views.DiningTypeList.as_view(), name='diningtype_list'),
    path('specialcategories', views.SpecialCategoryList.as_view(), name='specialcategory_list'),
]
