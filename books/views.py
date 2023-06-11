from rest_framework import viewsets, permissions, generics
from .models import Book, ReadLater
from accounts.models import CustomUser
from .serializers import BookSerializer, ReadlaterSerializer
from utils.permissions import IsOwner


class Booklist(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated, )


class BookDetail(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwner, )


class BookCreate(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated, )


class AddToLater(generics.CreateAPIView):
    serializer_class = ReadlaterSerializer
    permission_classes = (permissions.IsAuthenticated, )


class ReadToLaterDetail(viewsets.ModelViewSet):
    user = CustomUser.objects.get(pk=pk)
    queryset = ReadLater.objects.filter()
