from django.shortcuts import render
from rest_framework.generics import ListAPIView  # get uchun ruxsat --> o'qish uchun
from main.models import Book
from .serializer import BookSerializer

# Create your views here.


class BookApiView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


