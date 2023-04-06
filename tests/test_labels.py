from django.test import TestCase
from django.contrib.auth.models import User
from users.models import User
from labels.models import Labels


class LabelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name='test',
            last_name='testoff',
            username='testuser',
            password='ivan1234'
        )
        self.user.save()

        self.label = Labels(name='Test Label')
        self.label.save()

    def test_label_creation(self):
        label = Labels.objects.create(
            name='Another Label')
        self.assertEqual(label.name, 'Another Label')


    def test_label_str_method(self):
        self.assertEqual(str(self.label), 'Test Label')

    
    def test_update_label(self):
        self.label.name = 'Updated Label'
        self.label.save()
        updated_label = Labels.objects.get(pk=self.label.pk)
        self.assertEqual(updated_label.name, 'Updated Label')


    def test_label_deletion(self):
        self.label.delete()
        self.assertFalse(Labels.objects.filter(name='Test Label').exists())
