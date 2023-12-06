from django.db import models
import json
# Create your models here.


class DataFile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(
        upload_to='files/', content_type=['csv'], max_upload_size=1000000)

    def __str__(self):
        return self.name


class ManualDatas(models.Model):
    name = models.Charfield(max_length=100)
    description = models.TextField()
    heading1 = models.CharField(max_length=100)
    heading2 = models.CharField(max_length=100)

