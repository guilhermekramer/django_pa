from django.db import models
from categories.models import Category
from user.models import User


class Gasto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name="gastos", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name="gastos", on_delete=models.CASCADE, default=None)
