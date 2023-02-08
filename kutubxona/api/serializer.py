from rest_framework import serializers

from main.models import Book


# Json formatga o'tkazadi
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'category')