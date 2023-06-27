from django.db import models
from django.conf import settings

TYPES = [
    ('BE', 'Back-end'),
    ('FE', 'Front-end'),
    ('IOS', 'iOS'),
    ('ANDROID', 'Android')
]

class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)
    type = models.CharField(choices=TYPES, max_length=10)
    #avoide deletions from other user
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='project_created_by') 

