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

        self.user2 = User.objects.create_user(
            first_name='Name2',
            last_name='Last_name2',
            username='testuser2',
            password='testpass1234'
        )

    def test_create_user(self):
        response = self.client.post(reverse('users:create'), {
            'username': 'newuser',
            'password1': 'newpass123',
            'password2': 'newpass123',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        print(response.content)
        self.assertContains(response, 'User account created successfully')
        self.assertRedirects(response, reverse('login'))

    def test_update_user(self):
        self.client.login(username='testuser', password='testpass123')
        url = reverse('users:update', args=[self.user.id])
        form_data = {
            'username': 'testuser3',
            'first_name': 'Name3',
            'last_name': 'LastName3',
            'password1': 'testpass123',
            'password2': 'testpass123',
        }
        response = self.client.post(url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'User updated')
        self.assertRedirects(response, reverse('login'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'testuser3')

    def test_delete_user(self):
        self.client.login(username='testuser', password='testpass123')
        url = reverse('users:delete', args=[self.user.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('users:users'))
        self.assertFalse(User.objects.filter(username='testuser').exists())

    def test_delete_another_user(self):
        self.client.login(username='testuser', password='testpass123')
        url = reverse('users:delete', args=[self.user2.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='testuser2').exists())
