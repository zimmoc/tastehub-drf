from rest_framework import serializers
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.author

    class Meta:
        model = Recipe
        fields = [
            'id', 'author', 'created_at', 'updated_at', 'title', 'description',
            'image', 'ingredients', 'instructions', 'is_owner'
        ]