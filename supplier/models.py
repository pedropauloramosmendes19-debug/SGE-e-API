from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
