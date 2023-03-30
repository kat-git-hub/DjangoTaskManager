from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from labels.models import Labels

class DeleteLabelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        self.label = Labels.objects.create(
            name='Test Label',
            user=self.user
        )

    def test_delete_label(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(reverse('delete-label', kwargs={'pk': self.label.pk}))
        self.assertRedirects(response, reverse('labels-list'))
        self.assertFalse(Labels.objects.filter(pk=self.label.pk).exists())
