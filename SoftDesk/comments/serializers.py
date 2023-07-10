from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "description",
            "author_user_id",
            "issue_id",
            "created_time",
        ]
        read_only_fields = ("created_time",)


class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = fields = [
            "id",
            "description",
            "author_user_id",
            "issue_id",
            "created_time",
        ]
