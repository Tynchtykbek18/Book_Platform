from django.core.validators import MaxValueValidator
from django.db import models
from accounts.models import CustomUser
from books.models import Book


class Grade(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='grades')
    to_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='grades')
    grade = models.PositiveIntegerField(validators=[MaxValueValidator(10)])

    class Meta:
        verbose_name = 'оценка книги'
        verbose_name_plural = 'оценки книги'


class Comment(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='comments')
    to_book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.TextField(max_length=200, verbose_name='comment')

    class Meta:
        verbose_name = 'комментарии'
        verbose_name_plural = 'комментарии'



