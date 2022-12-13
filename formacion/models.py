from statistics import mode
from django.db import models


# Create your models here.
# class Areas(models.Model):
#     description = models.CharField(max_length=100)

#     def __str__(self):
#         return self.description

UNIVERSITARIO = 'UNI'
CURSO = 'CUR'
AYUDANTIA = 'AYU'

TYPE_CHOICES = (
    (UNIVERSITARIO, 'Universitario'),
    (CURSO, 'Curso'),
    (AYUDANTIA, 'Ayudantia'),
    )

    

class Formacion(models.Model):
    year = models.IntegerField()
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    place = models.CharField(max_length=100)
    description = models.TextField(null=True)
    order = models.SmallIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.description