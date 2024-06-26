from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from profiles.models import Profile

class ProfileModelTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.other_user = User.objects.create_user(username='otheruser', password='testpass')
        self.profile = Profile.objects.get(owner=self.user)
        self.client.login(username='testuser', password='testpass')

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_create_profile(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpass')
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

    def test_retrieve_profiles_list(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)
        owners = [result['owner'] for result in response.data['results']]
        self.assertIn('testuser', owners)
        self.assertIn('otheruser', owners)

    def test_retrieve_profile_detail(self):
        response = self.client.get(f'/profiles/{self.profile.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['owner'], 'testuser')

    def test_update_profile(self):
        response = self.client.put(f'/profiles/{self.profile.id}', {'bio': 'Updated bio', 'name': 'Updated name'})
        self.assertEqual(response.status_code, 200)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.bio, 'Updated bio')
        self.assertEqual(self.profile.name, 'Updated name')

    def test_non_owner_cannot_update_profile(self):
        self.client.logout()
        self.client.login(username='otheruser', password='testpass')
        response = self.client.put(f'/profiles/{self.profile.id}', {'bio': 'Should not update', 'name': 'Should not update'})
        self.assertEqual(response.status_code, 403)
        self.profile.refresh_from_db()
        self.assertEqual(self.profile.bio, '')
        self.assertEqual(self.profile.name, '')
