# malumotlarni json formatga o'tkazib beradi
from rest_framework import serializers
from .models import Blog
from django.contrib.auth import get_user_model

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'body', 'created_at', 'author')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", 'username',)





