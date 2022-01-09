from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .models import Todo

"""
Test classes are created based on view classes

"""

class TodosApiTestCase(APITestCase):

    def create_todos(self):

        todo = {"title":"Hello", "desc":"Test"}
        response=self.client.post(reverse("todos"), todo)
        return response

   

    def authenticate(self):
        user = {

                "username":"awadh",
                "email": "email@gmail.com",
                "password": "password@1"
        }
        self.client.post(reverse("register"), user )
        response = self.client.post(reverse("login"), {"email":"email@gmail.com",
                                                        "password": "password@1"      
                                                         })

        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {response.data['token']}")



class TestTodos(TodosApiTestCase):

    def test_create_todo_with_no_authentication(self):
      response = self.create_todos()
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    
    def test_create_post_with_authentication(self):
      self.authenticate()
      previous_todo_count = Todo.objects.all().count()
      response = self.create_todos()
      self.assertEqual(Todo.objects.all().count(), previous_todo_count+1)
      self.assertEqual(response.status_code, status.HTTP_201_CREATED)
      self.assertEqual(response.data['title'], "Hello")
      self.assertEqual(response.data["desc"], "Test")
      

    def test_retrieve_all_todos(self):
       self.authenticate()
       response =  self.client.get(reverse('todos'))
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertIsInstance(response.data['results'],list)
        #making a request
       resp=response = self.create_todos()
       self.assertIsInstance(resp.data['id'], int)



class TestTodoDetailItem(TodosApiTestCase):

    def test_get_one_item(self):

      self.authenticate()
      todo = self.create_todos()
      response = self.client.get(reverse("todo", kwargs = {"id" : todo.data['id']}))

      self.assertEqual(response.status_code, status.HTTP_200_OK)
      item = Todo.objects.get(todo.data['id'])
      self.assertEqual(item.title, todo.data['title'])

        

   