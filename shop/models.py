from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    points = models.PositiveIntegerField()

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
