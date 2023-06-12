from django.http import HttpResponse
from rest_framework import viewsets, permissions, generics
from rest_framework.generics import RetrieveAPIView

from .models import Book, ReadLater
from .serializers import BookSerializer, ReadLaterSerializer, AddToReadLater
from utils.permissions import IsOwner


class BookList(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated, )


class BookDetail(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwner, )


class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (permissions.IsAuthenticated, )



class ReadLaterListView(generics.ListAPIView):
    serializer_class = ReadLaterSerializer

    def get_queryset(self):
        user = self.request.user
        return ReadLater.objects.filter(owner=user)



class AddToLaterView(generics.CreateAPIView):
    serializer_class = AddToReadLater
    permission_classes = (permissions.IsAuthenticated, )
