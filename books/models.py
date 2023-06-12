from django.db import models
from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Book(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=30, verbose_name='название книги')
    description = models.TextField(max_length=100, verbose_name='описание книги')
    author = models.CharField(max_length=50, verbose_name='автор книги')
    cover = models.ImageField(verbose_name='обложка книги', upload_to='static/book/covers')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    book_file = models.FileField(blank=True, verbose_name=' книга в PDF формате', upload_to='./pdf')
    book_audio = models.FileField(blank=True, verbose_name='книга в аудио формате', upload_to='static/book/audio')
    read_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class ReadLater(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='read_later_user')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='read_later_book')
