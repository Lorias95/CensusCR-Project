from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=100)
    id_people = models.CharField(max_length=15)
    place = models.CharField(max_length=15)
    table = models.CharField(max_length=15)
    venc_id = models.CharField(max_length=15)

    class Meta:
        db_table = "people"


def __str__(self):
    return self.name

