from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer
from users.models import Contributor
from rest_framework.permissions import IsAuthenticated


class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        contributor= Contributor.objects.filter(user=self.request.user)
        #contributor_query = Project.objects.filter(project_contributor__in = contributor)
        #author_query = Project.objects.filter(author_user_id = self.request.user)
        return (Project.objects.filter(project_contributor__in = contributor)&Project.objects.filter(author_user_id = self.request.user).distinct())
    
    # def update(self, request, *args, **kwargs):
    #     data = request.data.copy()
    #     request.data['author_user_id'] = request.user.pk
    #     serializer = self.serializer_class(data = data)
    #     return 