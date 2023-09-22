from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length = 100)
    car_image = models.ImageField(upload_to='')
    description = models.TextField()
    type = models.CharField(max_length = 100)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name



