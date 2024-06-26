from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from recipes.models import Recipe
from comments.models import Comment

class CommentModelTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='testpass')
        self.recipe = Recipe.objects.create(owner=self.user, title='Test Recipe', description='Test description')
        self.comment = Comment.objects.create(owner=self.user, recipe=self.recipe, content='Test comment')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def tearDown(self):
        Comment.objects.all().delete()
        Recipe.objects.all().delete()
        User.objects.all().delete()

    def test_create_comment(self):
        response = self.client.post('/comments/', {'recipe': self.recipe.id, 'content': 'Another comment'})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Comment.objects.count(), 2)
        comment = Comment.objects.get(id=response.data['id'])
        self.assertEqual(comment.content, 'Another comment')
        self.assertEqual(comment.recipe, self.recipe)
        self.assertEqual(comment.owner, self.user)

    def test_retrieve_comments_list(self):
        response = self.client.get('/comments/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['content'], 'Test comment')

    def test_retrieve_comment_detail(self):
        response = self.client.get(f'/comments/{self.comment.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['content'], 'Test comment')

    def test_update_comment(self):
        response = self.client.put(f'/comments/{self.comment.id}', {'content': 'Updated comment'})
        self.assertEqual(response.status_code, 200)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Updated comment')

    def test_delete_comment(self):
        response = self.client.delete(f'/comments/{self.comment.id}')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Comment.objects.count(), 0)

    def test_non_owner_cannot_update_comment(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpass')
        response = self.client.put(f'/comments/{self.comment.id}', {'content': 'Should not update'})
        self.assertEqual(response.status_code, 403)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, 'Test comment')

    def test_non_owner_cannot_delete_comment(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpass')
        response = self.client.delete(f'/comments/{self.comment.id}')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Comment.objects.count(), 1)

