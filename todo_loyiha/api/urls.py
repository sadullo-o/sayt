from django.urls import path
from .views import ListTodo, DetailView
urlpatterns = [
    path('todos/', ListTodo.as_view()),# api/v1/todos
    path('todos/<int:pk>', DetailView.as_view())
]
