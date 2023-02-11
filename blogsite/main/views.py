from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .permissions import AvtorgaRuxsat
from .serializers import BlogSerializer
from .models import Blog
# ListAPIView  --> barcha malunmotlarni chiqaradi
# RetrieveAPIView --> alohida 1 ta malumot chiqaradi
# Create your views here.


# class BlogList(ListAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer
#
#
# class DetailView(RetrieveAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# permissions.IsAuthenticated oddiy foydalanuvchilar uchun ham mumkin
# permissions.IsAdminUser   faqat sayt adminlari uchun mumkin
# permissions.IsAuthenticatedOrReadOnly   barcha uchun o'qishga ruxsat bor lekin faqat login qilgan uchun o'zgartirish yoki create qilishga ruxsat bor


class BlogList(ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class DetailView(RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (AvtorgaRuxsat, )
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer