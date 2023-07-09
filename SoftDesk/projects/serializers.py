from .models import Project
from rest_framework import serializers
from issues.models import Issues
from issues.serializers import IssuesSerializer


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id',
            'title',
            'description',
            'type',
            'author_user_id',
            'project_contributor',
            'related_issues'
        ]
        read_only_fields = ('author_user_id', 'project_contributor')

    def create(self, validated_data):
        request = self.context.get("request")
        author = request.user     

        project = Project.objects.create(
            title=validated_data['title'], 
            description= validated_data['description'], 
            type=validated_data['type'], 
            author_user_id = author
        )

        project.save()
        return project

class ProjectDetailSerializer(serializers.ModelSerializer):
    related_issues = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = fields = [
            'id',
            'title',
            'description',
            'type',
            'author_user_id',
            'project_contributor',
            'related_issues',
        ]

    def get_related_issues(self, instance):
        queryset = Issues.objects.filter(project_id = instance.id)
        serializer = IssuesSerializer(queryset, many = True)
        return serializer.data