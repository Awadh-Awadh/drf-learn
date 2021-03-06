from django.contrib import auth
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework import authentication, serializers, status, permissions
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model


'''
GenericApiView helps in handling all the http requests
'''
class GetCurrentUser(GenericAPIView):
    permissions_classes  = (permissions.IsAuthenticated,)
  
    def get(self, request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response({"user": serializer.data})


class RegisterApiView(GenericAPIView):
  authentication_classes = []

  serializer_class = RegisterSerializer

  def post(self, request):
    serializer = self.serializer_class(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginApiView(GenericAPIView):
    '''
    The default authentication in settings will always try to protect all the views and there some views 
    which we may not want django_restframework to first try to authenticate a user before it can give access to the 
    view itself. For those classes we may want to override that action by setting the authentication_classes as a list
    '''
    authentication_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        email=request.data.get('email', None)
        password=request.data.get('password', None)
        user = authenticate(username=email, password=password)
        print(user)        
        if user:
          print("awadh")
          """
          install pyjwt
          generate an authentication token

          """
          serializer = self.serializer_class(user)
          return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)