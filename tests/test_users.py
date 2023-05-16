from django.urls import reverse
from django.test import TestCase
from users.models import User


class TestUsers(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name='Name1',
            last_name='Last_name1',
            username='testuser',
            password='testpass123')

    def test_create_user(self):
        response = self.client.post(reverse('users:create'), {
            'username': 'newuser',
            'password1': 'newpass123',
            'password2': 'newpass123',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    def test_update_user(self):
        self.client.login(username='testuser', password='testpass123')
        url = reverse('users:update', args=[self.user.id])
        form_data = {
            'username': 'testuser2',
            'first_name': 'Name_update',
            'last_name': 'LastName_update',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        response = self.client.post(url, data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'testuser2')

    def test_delete_user(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('users:delete', args=[self.user.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:users'))
        self.assertFalse(User.objects.filter(username=self.user).exists())
