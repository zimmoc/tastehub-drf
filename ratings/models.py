from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe

VALUE_CHOICES = ((0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'))
class Rating(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    recipe = models.ForeignKey(Recipe, related_name='ratings',
                               on_delete=models.CASCADE)
    value = models.IntegerField(choices=VALUE_CHOICES,
                                null=True, blank=True, default=None)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'recipe']

    def __str__(self):
        return f"{self.owner} gave a {self.value} to {self.recipe}"

