from django.urls import path
from todos import views


urlpatterns = [
    path('create', views.TodoApiCreate.as_view(), name='create')
]
