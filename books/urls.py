from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookView, BookDetail


router = DefaultRouter()
router.register('books', BookView)
router.register('book_detail', BookDetail)


urlpatterns = [
    path('', include(router.urls)),
]