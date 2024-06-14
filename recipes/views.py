from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from tastehub_drf.permissions import IsOwnerOrReadOnly
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
        ratings_count = Count('ratings', distinct=True),
        ratings_average=Avg('ratings__value')
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter
    ]
    search_fields = [
        'owner__username',
        'title',
        'ingredients',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'created_at',
        'ratings_count',
        'ratings_average',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RecipeSerializer
    queryset = Recipe.objects.annotate(
        comments_count = Count('comment', distinct=True),
        likes_count = Count('likes', distinct=True),
    ).order_by('-created_at')