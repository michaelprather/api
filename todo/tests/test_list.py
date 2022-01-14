from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestTodoList(APITestCase):
    def setUp(self):
        """
        Create mocked resources
        """
        url = reverse('todo-list')
        self.client.post(url, {'task': 'Read a book'}, format='json')
        self.client.post(url, {'task': 'Go for a walk', 'completed': True}, format='json')
        self.client.post(url, {'task': 'Take a nap'}, format='json')

    def test_list_todos(self):
        """
        A list of todos can be fetched
        """
        url = reverse('todo-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_list_completed_todos(self):
        """
        A filtered list of completed todos can be fetched
        """
        url = '/todo/?completed=True'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_tasks(self):
        """
        Todos can be filtered by searching tasks
        """
        url = '/todo/?search=nap'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
