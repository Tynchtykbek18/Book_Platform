from rest_framework import serializers

from ratings.serializers import GradeSerializer, CommentSerializer
from .models import Book, ReadLater


class BookSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    average_grade = serializers.SerializerMethodField()
    book_file = serializers.FileField(max_length=None, use_url=True)

    def get_average_grade(self, obj):
        # Расчет средней оценки книги
        grades = obj.grades.all()
        if grades:
            total_grades = sum([grade.grade for grade in grades])
            average_grade = total_grades / len(grades)
            return average_grade
        else:
            return None

    class Meta:
        model = Book
        fields = (
            'id', 'owner', 'title', 'description', 'author', 'cover', 'category', 'book_file', 'book_audio', 'grades',
            'comments', 'average_grade')


class ReadlaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadLater
        fields = '__all__'
