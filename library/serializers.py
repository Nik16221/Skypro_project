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
    def validate(self, data):
        active_books = data.get('active_books')
        if len(active_books) > 3:
            raise ValueError('Превышено максимальное число книг! (3)')
        return super().validate(data)

    class Meta:
        model = Reader
        fields = '__all__'
