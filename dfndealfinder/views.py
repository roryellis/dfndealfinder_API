from rest_framework import generics
from .serializers import RestaurantSerializer, SpecialSerializer
from .models import Restaurant, Special, DiningType, CuisineType


class RestaurantList(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class RestaurantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class SpecialList(generics.ListCreateAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer


class SpecialDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Special.objects.all()
    serializer_class = SpecialSerializer

# class DiningTypeList(generics.ListCreateAPIView):
#     queryset = DiningType.objects.all()
#     serializer_class = DiningTypeSerializer


# class DiningTypeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = DiningType.objects.all()
#     serializer_class = DiningTypeSerializer


# class CuisineTypeList(generics.ListCreateAPIView):
#     queryset = CuisineType.objects.all()
#     serializer_class = CuisineTypeSerializer


# class CuisineTypeDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = CuisineType.objects.all()
#     serializer_class = CuisineTypeSerializer
