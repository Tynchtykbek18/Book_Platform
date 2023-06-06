from rest_framework import viewsets

from utils.permissions import IsOwner
from .models import CustomUser
from .serializers import UserSerializer


class UserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwner, )
