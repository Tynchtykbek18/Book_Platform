from rest_framework import serializers
from .models import Book
from ratings.models import Grade, Comment


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('owner', 'grade')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('owner', 'comment_text')


class BookSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    average_grade = serializers.SerializerMethodField()

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
