from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from utils.permissions import IsOwner
from .models import Category, Book
from .serializers import BookSerializer


class BookView(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )



class BookDetail(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwner, )


class BookCreate(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )
