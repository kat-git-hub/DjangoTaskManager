from users.models import User
from django.urls import reverse
from labels.models import Labels
from django.test import TestCase


class LabelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name='test',
            last_name='testoff',
            username='testuser',
            password='testpass123'
        )
        self.user.save()

        self.label = Labels(name='Test Label')
        self.label.save()

    def test_label_creation(self):
        self.client.login(username='testuser', password='testpass123')
        url = reverse('labels:create')
        data = {'name': 'Another Test Label'}
        response = self.client.post(url, data, follow=True)
        self.assertContains(response, 'Label created successfully')
        self.assertEqual(response.status_code, 200)

    def test_labels_list(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('labels:labels'))
        self.assertEqual(response.status_code, 200)

    def test_label_str_method(self):
        self.assertEqual(str(self.label), 'Test Label')

    def test_update_label(self):
        self.client.login(username='testuser', password='testpass123')
        url = reverse('labels:update', kwargs={'pk': 1})
        data = {'name': 'Updated Test Label'}
        response = self.client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Label updated')
        updated_label = Labels.objects.get(pk=self.label.pk)
        self.assertEqual(updated_label.name, 'Updated Test Label')

    def test_label_deletion(self):
        self.label.delete()
        self.assertFalse(Labels.objects.filter(name='Test Label').exists())
