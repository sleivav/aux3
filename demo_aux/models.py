from django.contrib.auth.models import User
from django.db import models


class Owner(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    name = models.CharField(max_length=40)


class Farm(models.Model):
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(Owner, models.SET_NULL, null=True, blank=True)


# Create your models here.
class FarmAnimal(models.Model):
    animal_name = models.CharField(max_length=15)
    number_legs = models.IntegerField(default=4)
    farm = models.ForeignKey(Farm, related_name='animal',
                             on_delete=models.SET_NULL,
                             blank=True,
                             null=True)
    image = models.ImageField(upload_to='fotos', default='fotos/404.jpg')

    def __str__(self):
        return self.animal_name