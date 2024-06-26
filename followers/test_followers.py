# followers/tests/test_followers.py

from django.contrib.auth.models import User
from django.db import IntegrityError, transaction
from django.test import TestCase
from rest_framework.test import APIClient
from followers.models import Follower

class FollowerModelTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='testpass')
        self.third_user = User.objects.create_user(username='thirduser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def tearDown(self):
        Follower.objects.all().delete()
        User.objects.all().delete()

    def test_create_follower(self):
        response = self.client.post('/followers/', {'followed': self.other_user.id})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Follower.objects.count(), 1)
        follower = Follower.objects.get(id=response.data['id'])
        self.assertEqual(follower.owner, self.user)
        self.assertEqual(follower.followed, self.other_user)

    def test_retrieve_followers_list(self):
        Follower.objects.create(owner=self.user, followed=self.other_user)
        response = self.client.get('/followers/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['owner'], 'testuser')

    def test_retrieve_follower_detail(self):
        follower = Follower.objects.create(owner=self.user, followed=self.other_user)
        response = self.client.get(f'/followers/{follower.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['owner'], 'testuser')

    def test_delete_follower(self):
        follower = Follower.objects.create(owner=self.user, followed=self.other_user)
        response = self.client.delete(f'/followers/{follower.id}')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Follower.objects.count(), 0)

    def test_cannot_follow_twice(self):
        Follower.objects.create(owner=self.user, followed=self.other_user)
        try:
            with transaction.atomic():
                response = self.client.post('/followers/', {'followed': self.other_user.id})
        except IntegrityError:
            response = self.client.post('/followers/', {'followed': self.other_user.id})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(Follower.objects.count(), 1)
        self.assertIn('possible duplicate', response.data['detail'])

    def test_non_owner_cannot_delete_follower(self):
        follower = Follower.objects.create(owner=self.user, followed=self.other_user)
        self.client.logout()
        self.client.login(username='thirduser', password='testpass')
        response = self.client.delete(f'/followers/{follower.id}')
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Follower.objects.count(), 1)
