from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer
from .permissions import CommentPermisson
from projects.mixins import MultipleSerializerMixin


class CommentViewset(MultipleSerializerMixin, viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    detail_serializer_class = CommentDetailSerializer
    permission_classes = [
        CommentPermisson,
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs["issue_pk"])
