from django.db.models import Count
from rest_framework import generics, permissions
from tastehub_drf.permissions import IsOwnerOrReadOnly
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
        ratings_count = Count('ratings', distinct=True)
    ).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
    ).order_by('-created_at')