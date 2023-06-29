from .models import Project
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        field = [
            'id',
            'title',
            'description',
            'type',
            'author_user_id',
            'project_contributor',
        ]
        read_only_fields = ('author_user_id',)

    def create(self, validated_data):
        author = None
        request = self.context.get("request")
        if request and hasattr(request, "user"):
            author = request.user     
        
        title = validated_data['title']
        description = validated_data['description']
        type = validated_data['type']

        project = Project.objects.create(
            title, description, type, author
        )

        project.save()
        return project
    