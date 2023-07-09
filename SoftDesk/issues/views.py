from rest_framework import viewsets, permissions
from projects import models, mixins
from .serializers import IssuesSerializer, IssuesDetailSerializer
from .models import Issues
from .permissions import IssuePermisson

class IssuesViewset(mixins.MultipleSerializerMixin,viewsets.ModelViewSet):
    serializer_class = IssuesDetailSerializer
    detail_serializer_class = IssuesDetailSerializer
    permission_classes=[permissions.IsAuthenticated, IssuePermisson]

    def get_queryset(self):
        return Issues.objects.filter(project_id=self.kwargs['project_pk'])
    
