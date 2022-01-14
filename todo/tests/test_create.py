from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todo.models import ToDo


class TestTodoCreate(APITestCase):
    _url = reverse('todo-list')

    def test_create_todo(self):
        """
        Todos can be created
        """
        task = 'Go for a walk'
        data = {'task': task}
        response = self.client.post(self._url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ToDo.objects.count(), 1)
        self.assertEqual(ToDo.objects.get().task, task)

    def test_requires_task(self):
        """
        Task is required
        """
        response = self.client.post(self._url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ToDo.objects.count(), 0)

    def test_task_cannot_be_empty(self):
        """
        Tasks cannot be empty
        """
        data = {'task': ''}
        response = self.client.post(self._url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(ToDo.objects.count(), 0)

    def test_special_chars(self):
        """
        Tasks can contain escaped special chars
        """
        task = '\*this\.\{is\$=a\\string/'
        data = {'task': task}
        response = self.client.post(self._url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ToDo.objects.count(), 1)
        self.assertEqual(ToDo.objects.get().task, '\*this\.\{is\$=a\\string/')
