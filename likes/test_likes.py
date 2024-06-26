from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from recipes.models import Recipe
from likes.models import Like
from django.db import IntegrityError, transaction

class LikeModelTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='testpass')
        self.recipe = Recipe.objects.create(owner=self.user, title='Test Recipe', description='Test description')
        self.like = Like.objects.create(owner=self.user, recipe=self.recipe)
        self.client.login(username='testuser', password='testpass')

    def tearDown(self):
        Like.objects.all().delete()
        Recipe.objects.all().delete()
        User.objects.all().delete()

    def test_create_like(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpass')
        response = self.client.post('/likes/', {'recipe': self.recipe.id})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Like.objects.count(), 2)
        like = Like.objects.get(id=response.data['id'])
        self.assertEqual(like.owner.username, 'otheruser')
        self.assertEqual(like.recipe, self.recipe)

    def test_retrieve_likes_list(self):
        response = self.client.get('/likes/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['owner'], 'testuser')

    def test_retrieve_like_detail(self):
        response = self.client.get(f'/likes/{self.like.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['owner'], 'testuser')

    def test_delete_like(self):
        response = self.client.delete(f'/likes/{self.like.id}')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Like.objects.count(), 0)

    def test_cannot_like_twice(self):
        try:
            with transaction.atomic():
                response = self.client.post('/likes/', {'recipe': self.recipe.id})
                self.assertEqual(response.status_code, 400)
        except IntegrityError:
            self.assertEqual(Like.objects.count(), 1)

    def test_non_owner_cannot_delete_like(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpass')
        response = self.client.delete(f'/likes/{self.like.id}')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Like.objects.count(), 1)
