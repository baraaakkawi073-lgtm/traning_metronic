from django.db import models
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.name

# Create your models here.
