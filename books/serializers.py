from rest_framework import serializers
from .models import Book
from ratings.models import Grade, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        grades = representation.pop('grades')
        comments = representation.pop('comments')
        representation['grades'] = len(grades)
        representation['comments'] = len(comments)
        return representation
