from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookDetail, BookCreate, ReadLaterListView,  AddToLaterView


router = DefaultRouter()
router.register('books', BookList)
router.register('book_detail', BookDetail)


urlpatterns = [
    path('', include(router.urls)),
    path('addbook/', BookCreate.as_view()),
    path('addto/readlater/', AddToLaterView.as_view()),
    path('list/readlater/', ReadLaterListView.as_view()),
]

