from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import ToDo


class TestTodoUpdate(APITestCase):
    _url = ''

    def setUp(self):
        """
        Create a mocked resource that can be updated
        """
        url = reverse('todo-list')
        data = {'task': 'Read a book'}
        response = self.client.post(url, data, format='json')
        self._url = reverse('todo-detail', kwargs={'pk': response.data.get('id')})

    def test_update_task(self):
        """
        Tasks can be updated
        """
        task = 'Go for a walk'
        data = {'task': task}
        response = self.client.patch(self._url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDo.objects.get().task, task)

    def test_complete_todo(self):
        """
        Todos can be completed
        """
        data = {'completed': True}
        response = self.client.patch(self._url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(ToDo.objects.get().completed, True)
