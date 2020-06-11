from rest_framework import serializers
from .models import Restaurant, Special, CuisineType, DiningType, SpecialCategory

class RestaurantMiniSerializer(serializers.ModelSerializer):
    restaurant_url = serializers.ModelSerializer.serializer_url_field(
        view_name='restaurant_detail')
    
    cuisine = serializers.StringRelatedField(many=True)
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'cuisine', 'restaurant_url')

class SpecialSerializer(serializers.ModelSerializer):
    restaurant = RestaurantMiniSerializer()

    category = serializers.StringRelatedField(many=True)

    class Meta:
        model = Special
        fields = ('id', 'restaurant', 'title', 'description', 'promo_image', 'category', 'daily_special',
                  'special_day', 'limited_time', 'start_date', 'end_date',)


class RestaurantSerializer(serializers.ModelSerializer):

    specials = SpecialSerializer(many=True)

    dining_options = serializers.StringRelatedField(many=True)

    cuisine = serializers.StringRelatedField(many=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address', 'city', 'state', 'zip', 'dining_options', 'cuisine',
                  'description', 'restaurant_image', 'website_url', 'specials',)
        lookup_field = 'name'
