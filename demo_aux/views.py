from django.shortcuts import render

from demo_aux.models import FarmAnimal


def primera_pagina(request):
    farm_animals = FarmAnimal.objects.all()
    return render(request, 'demo_aux/index.html',
                  {'farm_animals': farm_animals})
