from django.db import models
from django.db.models import SET_NULL
from users.models import User
from categories.models import Category
from views.models import View


class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    sku = models.CharField(max_length=12, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)

    views = models.ManyToManyField(View)

    def __str__(self):
        return self.name
