from django.contrib import auth
from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
import jwt
from authentication.models import CustomUser
from django.conf import settings


class JwtAuthentication(BaseAuthentication):

    def authenticate(self, request):
      auth_header = get_authorization_header(request)
      auth_data = auth_header.decode('utf-8')
      auth_token = auth_data.split(" ")
      """
      splits the token string into bearer and token bearer being the zeroth index and token the fist index

      """
     
      if len(auth_token) != 2:
          raise exceptions.AuthenticationFailed("Invalid Token")

      token = auth_token[1]
      

      try: 
         print(token)      
         decoded = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
         print(decoded)
         username = decoded['username']
         user = CustomUser.objects.get(username=username)
         return (user, token)

      except jwt.ExpiredSignatureError as ex:
          raise exceptions.AuthenticationFailed("Token has expired please login again")
     

      except jwt.DecodeError:
          raise exceptions.AuthenticationFailed("Token is Invalid")
          
      except CustomUser.DoesNotExist:
          raise exceptions.AuthenticationFailed("User does not exist")

    