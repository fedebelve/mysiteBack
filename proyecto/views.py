import json
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from proyecto.models import Proyecto
from proyecto.serializers import ProyectoSerializer
from rest_framework.response import Response

# Create your views here.
class ListProyecto(generics.ListAPIView):
    serializer_class = ProyectoSerializer
    #queryset =  Proyecto.objects.all()
    model = serializer_class.Meta.model

    def get_queryset(self):
        tag = self.kwargs['tag']
        if tag == 'all':
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(tag__tag= tag.lower())
        return queryset.order_by('-order')

class Proyecto(generics.ListAPIView):
    serializer_class = ProyectoSerializer
    queryset =  Proyecto.objects.all()
    model = serializer_class.Meta.model


    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = self.model.objects.filter(pk=pk)
        return queryset
         