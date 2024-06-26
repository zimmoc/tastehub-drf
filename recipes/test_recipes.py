from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from recipes.models import Recipe
from rest_framework import status

class RecipeModelTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='testpass')
        self.recipe = Recipe.objects.create(
            owner=self.user,
            title='Test Recipe',
            description='Test description',
            ingredients=["Ingredient 1", "Ingredient 2"],
            instructions=["Step 1", "Step 2"]
        )
        self.client.login(username='testuser', password='testpass')

    def tearDown(self):
        Recipe.objects.all().delete()
        User.objects.all().delete()

    def test_create_recipe(self):
        data = {
            'title': 'New Recipe',
            'description': 'New description',
            'ingredients': ["Ingredient A", "Ingredient B"],
            'instructions': ["Step A", "Step B"]
        }
        self.client.logout()
        self.client.login(username='otheruser', password='testpass')
        response = self.client.post('/recipes/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 2)
        recipe = Recipe.objects.get(id=response.data['id'])
        self.assertEqual(recipe.title, 'New Recipe')
        self.assertEqual(recipe.owner, self.other_user)

    def test_retrieve_recipes_list(self):
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['title'], 'Test Recipe')

    def test_retrieve_recipe_detail(self):
        response = self.client.get(f'/recipes/{self.recipe.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Recipe')

    def test_update_recipe(self):
        data = {'title': 'Updated Recipe'}
        response = self.client.put(f'/recipes/{self.recipe.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.title, 'Updated Recipe')

    def test_delete_recipe(self):
        response = self.client.delete(f'/recipes/{self.recipe.id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Recipe.objects.count(), 0)

    def test_non_owner_cannot_update_recipe(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpass')
        data = {'title': 'Should not update'}
        response = self.client.put(f'/recipes/{self.recipe.id}', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.recipe.refresh_from_db()
        self.assertEqual(self.recipe.title, 'Test Recipe')

    def test_non_owner_cannot_delete_recipe(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpass')
        response = self.client.delete(f'/recipes/{self.recipe.id}')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Recipe.objects.count(), 1)
