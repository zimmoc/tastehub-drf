from rest_framework import generics
from tastehub_drf.permissions import IsOwnerOrReadOnly
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeList(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RecipeDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer