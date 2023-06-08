from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UserList, UserDetail, UserCreate


# router = DefaultRouter()
# router.register('users', UserView)


urlpatterns = [
    path('userlist/', UserList.as_view()),
    path('userdetail/<int:pk>/', UserDetail.as_view()),
    path('usercreate/', UserCreate.as_view()),
]