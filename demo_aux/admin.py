from django.contrib import admin

# Register your models here.
from demo_aux.models import FarmAnimal, Owner, Farm

admin.site.register(FarmAnimal)
admin.site.register(Owner)
admin.site.register(Farm)
