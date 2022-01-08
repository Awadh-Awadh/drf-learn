from django.shortcuts import render
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from todos.models import Todo
from todos.serializers import TodoSerializer


class TodoApiCreate(CreateAPIView):
    permissions_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)