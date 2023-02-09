from django.shortcuts import render
from .models import Todo
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import TodoSerializer
# Create your views here.


class ListTodo(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer



# https://todo.uz
# https://kundalikishlar.uz
# CORS headerd

# Yangiliklar sayti uchun backend api chiqarib qo'yish