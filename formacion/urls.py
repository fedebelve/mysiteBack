from django import views
from django.contrib import admin
from django.urls import path
from formacion.views import ListFormacion

urlpatterns = [
    path('', ListFormacion.as_view()),
]
