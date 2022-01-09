from django.urls import path
from todos import views


urlpatterns = [
    # path('create', views.TodoApiCreate.as_view(), name='create'),
    # path('list', views.ListTodos.as_view(), name = 'list')
    path("", views.TodosApi.as_view(), name='todos'),
    path("detail/<int:pk>", views.TodosDetailApi.as_view(), name = "todo")
]
