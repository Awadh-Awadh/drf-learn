from django.shortcuts import render
from rest_framework import serializers
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.models import Todo
from todos.serializers import TodoSerializer


class TodosApi(ListCreateAPIView):
    serializer_class = TodoSerializer
    permissions = (IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)




class TodosDetailApi(RetrieveUpdateDestroyAPIView):
      serializer_class = TodoSerializer
      permissions = (IsAuthenticated,)

      lookup_fields = ['pk']

      def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)


# class TodoApiCreate(CreateAPIView):
#     permissions_classes = (IsAuthenticated,)
#     serializer_class = TodoSerializer

#     def perform_create(self, serializer):
#         return serializer.save(owner=self.request.user)


# class ListTodos(ListAPIView):
#     permissions = (IsAuthenticated,)
#     serializer_class = TodoSerializer
#     '''
#     get_queryset will return all todos created by a certain useronly
    
#     '''
#     def get_queryset(self):
#         return Todo.objects.filter(owner=self.request.user)