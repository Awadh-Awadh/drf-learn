from django.shortcuts import render
from rest_framework import pagination, serializers
from rest_framework import permissions,filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from todos.models import Todo
from todos.serializers import TodoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from todos.pagination import CustomPageNumberPagination


class TodosApi(ListCreateAPIView):
    serializer_class = TodoSerializer
    permissions = (IsAuthenticated,)
    pagination_class = CustomPageNumberPagination

    '''
    django filters allow ordering and searching easier
    we need to specify filterBackends and filterset_fields, serach and odering fields
    With that we change append a query string in our to enable filtering,seraching and ordering
    eg = endpoint?id=1----> filtering
    eg = endpoint?search=Awadh----> searching
    eg = endpoint?ordering=id----> ordering
    
    '''
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ("id", "title", "is_complete", "desc")
    search_fields = ("id", "title", "is_complete", "desc")
    ordering_fields = ("id", "title", "is_complete", "desc")


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