from django.shortcuts import render
from rest_framework import generics
from formacion.models import Formacion
from formacion.serializers import FormacionSerializer

# Create your views here.
class ListFormacion(generics.ListAPIView):
    serializer_class = FormacionSerializer
    queryset =  Formacion.objects.all().order_by('-year')

