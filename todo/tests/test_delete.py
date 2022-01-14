from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import ToDo


class TestTodoDelete(APITestCase):
    _url = ''

    def setUp(self):
        """
        Create a mocked resource that can be deleted
        """
        url = reverse('todo-list')
        data = {'task': 'Read a book'}
        response = self.client.post(url, data, format='json')
        self._url = reverse('todo-detail', kwargs={'pk': response.data.get('id')})

    def test_delete_task(self):
        """
        Todos can be deleted
        """
        response = self.client.delete(self._url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ToDo.objects.count(), 0)
