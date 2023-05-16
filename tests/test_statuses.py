from users.models import User
from django.urls import reverse
from django.test import TestCase
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
        status = Status.objects.create(name='Another Status')
        self.assertTrue(isinstance(status, Status))
        self.assertEqual(status.name, 'Another Status')

    def test_status_str_method(self):
        self.assertEqual(str(self.status), 'Test Status')

    def test_update_status(self):
        self.status.name = 'Updated Status'
        self.status.save()
        updated_status = Status.objects.get(pk=self.status.pk)
        self.assertEqual(updated_status.name, 'Updated Status')

    def test_status_deletion(self):
        self.status.delete()
        self.assertFalse(Status.objects.filter(name='Test Status').exists())

    def test_user_can_create_status(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('statuses:create'), {'name': 'New Status'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Status.objects.filter(name='New Status').exists())

    def test_logout_redirect_to_main_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('statuses:statuses'))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main'))
