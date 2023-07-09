from django.db import models
from projects.models import Project
from users.models import User
from django.conf import settings


PRIORITY = [
    ('FAIBLE', 'Faible'),
    ('MOYEN', 'Moyen'),
    ('ELEVEE', 'Elevée')
]

TAG = [
    ('BUG', 'Bug'),
    ('AMELIORATION', 'Amélioration'),
    ('TACHE', 'Tâche')
]

STATUS = [
    ('A_FAIRE', 'A faire'),
    ('EN_COURS', 'En cours'),
    ('TERMINE', 'Terminé')
]

class Issues(models.Model):
    title = models.CharField(max_length=128)
    desc = models.CharField(max_length=255)
    tag = models.CharField(max_length=12, choices=TAG) 
    priority = models.CharField(max_length=8, choices=PRIORITY)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="related_issues" )
    status = models.CharField(max_length=10, choices=STATUS)
    author_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, related_name='issue_created_by')
    assignee_user_id = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="issue_assigned_to")
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title