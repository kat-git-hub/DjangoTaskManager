from users.models import User
from django.urls import reverse
from django.test import TestCase


class LoginTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            first_name='Name',
            last_name='Last_name',
            username='testuser',
            password='testpass123'
        )
        self.data = {
            'username': 'testuser',
            'password': 'testpass123'
        }

    def test_login_valid_account(self):
        response = self.client.post(reverse('login'), self.data, follow=True)
        self.assertRedirects(response, reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'You have successfully logged in')

    def test_login_invalid_account(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'general_pattern.html')
        self.assertNotContains(response, 'You have successfully logged in')
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('logout'), follow=True)
        self.assertRedirects(response, reverse('main'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertContains(response, 'You are logged out')
