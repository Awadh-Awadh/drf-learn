from django.contrib import auth
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate


'''
GenericApiView helps in handling all the http requests
'''


class RegisterApiView(GenericAPIView):

  serializer_class = RegisterSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(GenericAPIView):

    serializer_class = LoginSerializer
    def post(self, request):
        email=request.data.get('email')
        password=request.data.get('password')
        user=authenticate(username=email, password=password)

        if user:
          """
          install pyjwt
          generate an authentication token

          """