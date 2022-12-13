from rest_framework import serializers
from proyecto.models import Proyecto

class ProyectoSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(many=True)
    img = serializers.SerializerMethodField()

    class Meta:
        model = Proyecto
        fields = '__all__'

    def get_img(self,obj):
        path = obj.img.name
        request = self.context.get('request')
        #spliteado = path.split("/")[2]
        spliteado = path
        #url = (request.build_absolute_uri(path.split("/")[2])).replace("proyecto","img")
        url = (request.build_absolute_uri(path)).replace("proyecto","img")
        return url


    def to_representation(self, instance):
        data = super(ProyectoSerializer, self).to_representation(instance)
        last = Proyecto.objects.last()
        data['isLast'] = False
        if last.pk == data['id']:
            data['isLast'] = True

        return data