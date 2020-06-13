from django.db import models
from django.conf import settings
from time import time
# Create your models here.


def upload_image_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{instance.name}{round(time())}.{ext}'
    return f'images/{filename}'

class CuisineType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DiningType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SpecialCategory(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "SpecialCategories"

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    dining_options = models.ManyToManyField(
        DiningType,
        
    )
    cuisine = models.ManyToManyField(
        CuisineType,
        related_name='restaurants'
    )
    description = models.TextField()
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='restaurants'
    )
    restaurant_image = models.ImageField(upload_to=upload_image_name, blank=True)
    website_url = models.URLField()

    # Add timestamps
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Special(models.Model):
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='specials'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    promo_image = models.ImageField(upload_to=upload_image_name, blank=True)
    category = models.ManyToManyField(
        SpecialCategory,
        related_name='specials'
    )
    daily_special = models.BooleanField()
    DAY_CHOICES = [
        ('monday', 'monday'),
        ('tuesday', 'tuesday'),
        ('wednesday', 'wednesday'),
        ('thursday', 'thursday'),
        ('friday', 'friday'),
        ('saturday', 'saturday'),
        ('sunday', 'sunday'),
        ('weekdays', 'weekdays'),
        ('weekends', 'weekends'),
    ]
    special_day = models.CharField(
        max_length=10,
        choices=DAY_CHOICES,
        null=True,
        blank=True,
    )
    # monday = models.BooleanField()
    # tuesday = models.BooleanField()
    # wednesday = models.BooleanField()
    # thursday = models.BooleanField()
    # friday = models.BooleanField()
    # saturday = models.BooleanField()
    # sunday = models.BooleanField()
    limited_time = models.BooleanField()
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.name
