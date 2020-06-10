from rest_framework import serializers
from .models import Restaurant, Special, CuisineType, DiningType, SpecialCategory


class SpecialSerializer(serializers.ModelSerializer):
    restaurant = serializers.StringRelatedField()

    restaurant_url = serializers.ModelSerializer.serializer_url_field(
        view_name='restaurant_detail')

    category = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Special
        fields = ('id', 'restaurant', 'restaurant_url', 'title', 'description', 'promo_image', 'category', 'daily_special', 'monday', 'tuesday',
                  'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'limited_time', 'start_date', 'end_date',)


class RestaurantSerializer(serializers.ModelSerializer):

    specials = SpecialSerializer(many=True)

    restaurant_url = serializers.ModelSerializer.serializer_url_field(
        view_name='restaurant_detail')

    dining_options = serializers.StringRelatedField(many=True)

    cuisine = serializers.StringRelatedField(many=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'city', 'state', 'zip', 'dining_options', 'cuisine',
                  'description', 'restaurant_image', 'website_url', 'specials', 'restaurant_url')
        lookup_field = 'name'
