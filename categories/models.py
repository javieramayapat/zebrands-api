from django.db import models
from django.db.models import SET_NULL
from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.title
