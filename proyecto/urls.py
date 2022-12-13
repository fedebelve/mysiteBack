from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from proyecto.views import ListProyecto, Proyecto

urlpatterns = [
    path('<tag>', ListProyecto.as_view()),
    path('id/<pk>', Proyecto.as_view()),
]
