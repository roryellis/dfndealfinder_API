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
    # queryset = Special.objects.all()
    serializer_class = SpecialSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Special.objects.all()
        category = self.request.query_params.get('category', None)
        daily_special = self.request.query_params.get('daily_special', None)
        special_day = self.request.query_params.get('special_day', None)
        limited_time = self.request.query_params.get('limited_time', None)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        cuisine = self.request.query_params.get('cuisine', None)

        if category is not None:
            queryset = queryset.filter(category__name__icontains=category)
        if daily_special is not None:
            queryset = queryset.filter(daily_special=daily_special)
        if special_day is not None:
            queryset = queryset.filter(special_day__icontains=special_day)
        if limited_time is not None:
            queryset = queryset.filter(limited_time=limited_time)
        if start_date is not None:
            queryset = queryset.filter(start_date__lte=start_date)
        if end_date is not None:
            queryset = queryset.filter(end_date__gte=end_date)
        if cuisine is not None:
            queryset = queryset.filter(restaurant__cuisine__name__icontains=cuisine)
        return queryset


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
