from django.db import models
from django.contrib.auth.models import AbstractUser
from projects.models import Project

class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    def __str__(self):
        return self.email
    
class Contributor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_contributor')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_contributor')
