from rest_framework import serializers
from .models import Issues
from comments.models import Comment
from comments.serializers import CommentSerializer

class IssuesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Issues
        fields = [
            'id',
            'title',
            'desc',
            'tag',
            'priority',
            'project_id',
            'status',
            'author_user_id',
            'assignee_user_id',
            'created_time',
            'issue_comment',
        ]
        read_only_fields = ('author_user_id','project_id', 'created_time',)


class IssuesDetailSerializer(serializers.ModelSerializer):
    issue_comment = serializers.SerializerMethodField()
    class Meta:
        model = Issues
        fields = fields = [
            'id',
            'title',
            'desc',
            'tag',
            'priority',
            'project_id',
            'status',
            'author_user_id',
            'assignee_user_id',
            'created_time',
            'issue_comment'
        ]
    def get_issue_comment(self, instance):
        queryset = Comment.objects.filter(issue_id = instance.id)
        serializer = CommentSerializer(queryset, many = True)
        return serializer.data


