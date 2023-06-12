from rest_framework import serializers

from ratings.serializers import GradeSerializer, CommentSerializer
from .models import Book, ReadLater


class BookSerializer(serializers.ModelSerializer):
    grades = GradeSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    average_grade = serializers.SerializerMethodField()
    book_file = serializers.FileField(max_length=None, use_url=True)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def get_average_grade(self, obj):
        grades = obj.grades.all()
        if grades:
            total_grades = sum([grade.grade for grade in grades])
            average_grade = total_grades / len(grades)
            return average_grade
        else:
            return None

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class ReadLaterSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = ReadLater
        fields = '__all__'

    def to_representation(self, instance):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user = request.user
            if instance.owner == user:
                return super().to_representation(instance)

        return {}


class AddToReadLater(serializers.ModelSerializer):
    class Meta:
        model = ReadLater
        fields = '__all__'
