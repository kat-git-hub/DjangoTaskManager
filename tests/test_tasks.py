from django.test import TestCase
from django.urls import reverse
from users.models import User
from statuses.models import Status
from labels.models import Labels
from tasks.models import Task

class TaskTests(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(
            username='testuser1', 
            password='testpass123')
        self.user2 = User.objects.create_user(
            username='testuser2', 
            password='testpass123')
        self.status = Status.objects.create(name='New')
        self.label = Labels.objects.create(name='Important')
        self.task = Task.objects.create(
            name='Test Task', 
            status=self.status, 
            author=self.user1, 
            executor=self.user2, 
            description='Test description'
        )

    def test_task_list_view(self):
        url = reverse('tasks:tasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.task.name)
    
    # def test_task_detail_view(self):
    #     url = reverse('task_detail', args=[self.task.pk])
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, self.task.name)
    
    def test_task_create_view(self):
        self.client.login(username='testuser1', password='testpass123')
        url = reverse('tasks:create')
        data = {
            'name': 'New Task',
            'status': self.status.pk,
            'author': self.user1.pk,
            'executor': self.user2.pk,
            'description': 'New description',
            'labels': [self.label.pk]
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(name='New Task').exists())
    
    # # def test_task_update_view(self):
    # #     url = reverse('task_update', args=[self.task.pk])
    # #     data = {
    # #         'name': 'Updated Task',
    # #         'status': self.status.pk,
    # #         'author': self.user1.pk,
    # #         'executor': self.user2.pk,
    # #         'description': 'Updated description',
    # #         'labels': [self.label.pk]
    # #     }
    # #     response = self.client.post(url, data)
    # #     self.assertEqual(response.status_code, 302)
    # #     self.task.refresh_from_db()
    # #     self.assertEqual(self.task.name, 'Updated Task')
    
    # def test_task_delete_view(self):
    #     url = reverse('task_delete', args=[self.task.pk])
    #     response = self.client.post(url)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(Task.objects.filter(name='Test Task').exists())
