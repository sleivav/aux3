from django.urls import path

from demo_aux import views

urlpatterns = [
    path('primera_pagina', views.primera_pagina)
]
