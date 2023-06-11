from rest_framework import serializers

from ratings.models import Grade, Comment


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('owner', 'grade')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('owner', 'comment_text')