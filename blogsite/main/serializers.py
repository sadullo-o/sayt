# malumotlarni json formatga o'tkazib beradi
from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('id', 'title', 'body', 'created_at', 'author')






