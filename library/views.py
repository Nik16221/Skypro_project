from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from library.models import Reader, Book, Author
from library.serializers import AuthorSerializers, BookSerializers, ReaderSerializers


class AuthorView(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers

    def get_permissions(self):

        if self.action == ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

    def get_permissions(self):

        if self.action == ['list', 'retrieve']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ReaderView(ModelViewSet):
    queryset = Reader.objects.all()
    serializer_class = ReaderSerializers

    def get_permissions(self):

        if self.action == ['list', 'retrieve']:
            permission_classes = [IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [IsAdminUser, IsAuthenticated]
        return [permission() for permission in permission_classes]


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
