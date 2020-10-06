from django.test import TestCase, Client
from api.models import Task

class TaskTestCase(TestCase):

    def setUp(self):
        Task.objects.create(title='My First Task')

    def test_task_list(self):
        response = self.client.get('/api/task-list/')
        self.assertEqual(response.status_code, 200)

    def test_task_detail(self):
        task_id = Task.objects.get(pk=1).id
        response = self.client.get(f'/api/task-detail/{task_id}/')
        self.assertEqual(response.status_code, 200)

    def test_task_create(self):
        response = self.client.post('/api/task-create/', { 'title': 'New Task' }, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_task_update(self):
        task_id = Task.objects.get(pk=1).id
        response = self.client.post(f'/api/task-update/{task_id}/', { 'title': 'Task Updated!!' }, content_type='application/json')
        new_task = response.json()
        self.assertEqual(new_task['title'], 'Task Updated!!')

    def test_task_delete(self):
        task_id = Task.objects.get(pk=1).id
        response = self.client.delete(f'/api/task-delete/{task_id}/', content_type='application/json')
        self.assertEqual(response.status_code, 200)


        
