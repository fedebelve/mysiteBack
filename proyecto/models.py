from statistics import mode
from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.tag


class Proyecto(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    duration = models.CharField(max_length=80)
    tag = models.ManyToManyField(Tag)
    description = models.TextField()
    img = models.ImageField(null=True, upload_to='./')
    order = models.SmallIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title