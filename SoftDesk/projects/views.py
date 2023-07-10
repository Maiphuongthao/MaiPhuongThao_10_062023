from rest_framework import viewsets
from .models import Project
from .serializers import ProjectSerializer, ProjectDetailSerializer
from .permissons import ProjectPermisson
from users.models import Contributor
from rest_framework.permissions import IsAuthenticated


class MultipleSerializerMixin:
    def get_serializer_class(self):
        if (
            self.action == "retrieve"
            or self.action == "create"
            or self.action == "update"
            and self.detail_serializer_class is not None
        ):
            return self.detail_serializer_class
        return super().get_serializer_class()


class ProjectViewset(MultipleSerializerMixin, viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    detail_serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated, ProjectPermisson]

    def get_queryset(self):
        project_contributor = Contributor.objects.filter(user_id=self.request.user)
        author_set = Project.objects.filter(author_user_id=self.request.user)
        contributor_set = Project.objects.filter(
            project_contributor__in=project_contributor
        )

        return author_set | contributor_set
