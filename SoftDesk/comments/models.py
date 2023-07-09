from django.db import models
from issues.models import Issues
from django.conf import settings

class Comment(models.Model):
    description = models.CharField(max_length=128, blank=False)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='user_comment')
    issue_id = models.ForeignKey(Issues, on_delete=models.CASCADE, related_name='issue_comment')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return super(self.description).__str__()

