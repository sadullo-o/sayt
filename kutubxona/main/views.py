from django.shortcuts import render, HttpResponse
from .models import Book
# Create your views here.

def main(request):
    books = Book.objects.all()
    info = ''
    for i in books:
        info+= "<p>" + i.title + ' ' + i.description + ' ' + i.author + ' ' + i.cost + "</p> <br>"
    return HttpResponse(info)