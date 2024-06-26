from django.db import models
from django.contrib.auth.models import User
from django.db.models import JSONField


class Recipe(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/recipes/')
    ingredients = JSONField(blank=True, default=list, null=True)
    instructions = JSONField(blank=True, default=list, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} by {self.owner}"
