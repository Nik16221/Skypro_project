from rest_framework.viewsets import ModelViewSet
from library.serializers import *


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers


class ReaderView(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializers
