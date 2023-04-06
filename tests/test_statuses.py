from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import User
from statuses.models import Status


class StatusesTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name='test',
            last_name='testoff',
            username='testuser',
            password='ivan1234'
        )
        self.user.save()

        self.status = Status(name='Test Status')
        self.status.save()

    def test_status_creation(self):
        status = Status.objects.create(
            name='Another Status')
        self.assertEqual(status.name, 'Another Status')


    def test_status_str_method(self):
        self.assertEqual(str(self.status), 'Test Status')

    
    def test_update_label(self):
        self.status.name = 'Updated Status'
        self.status.save()
        updated_status = Status.objects.get(pk=self.status.pk)
        self.assertEqual(updated_status.name, 'Updated Status')


    def test_status_deletion(self):
        self.status.delete()
        self.assertFalse(Status.objects.filter(name='Test Status').exists())

    def test_status_view_logout(self):
        self.client.logout()
        response = self.client.get('/logout/')
        response = self.client.get(reverse('statuses:statuses'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/')


