from django.db import models

from item.models import Item

class Category(models.Model):
    name = models.CharField(max_length=255)
    items = models.ManyToManyField( Item, related_name='categories')

    def __str__(self):
        return self.name