from django.forms import ChoiceField
from rest_framework import serializers
from formacion.models import Formacion

class FormacionSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display')

    class Meta:
        model = Formacion
        fields = '__all__'