from django.db import models


class View(models.Model):
    viewed_at = models.DateTimeField(auto_now_add=True)
