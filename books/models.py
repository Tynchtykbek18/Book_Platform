from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=30, verbose_name='название книги')
    description = models.TextField(max_length=100, verbose_name='описание книги')
    author = models.CharField(max_length=50, verbose_name='автор книги')
    cover = models.ImageField(verbose_name='обложка книги', upload_to='/covers')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    book_file = models.FileField()

