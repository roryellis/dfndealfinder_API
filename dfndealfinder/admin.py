from django.contrib import admin
from .models import Restaurant, Special, CuisineType, DiningType, SpecialCategory

# Register your models here.
admin.site.register(Restaurant)
admin.site.register(Special)
admin.site.register(CuisineType)
admin.site.register(DiningType)
admin.site.register(SpecialCategory)
