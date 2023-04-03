from django.core.exceptions import ValidationError
from rest_framework import serializers
from library.models import Author, Reader, Book


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class ReaderSerializers(serializers.ModelSerializer):
    def validate_active_books(self, books: list) -> list:
        if len(books) > 3:
            raise ValidationError('Превышено максимальное число книг! (3)')
        return books

    class Meta:
        model = Reader
        fields = '__all__'
