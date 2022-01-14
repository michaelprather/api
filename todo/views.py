from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from todo.serializers import ToDoSerializer
from todo.models import ToDo


class ToDoList(generics.ListCreateAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['completed']
    search_fields = ['task']


class ToDoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
