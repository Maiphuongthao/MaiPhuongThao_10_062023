from django.db import models
from django.contrib.auth.models import AbstractUser
from projects.models import Project
from django.contrib.auth.base_user  import (BaseUserManager)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Veuillez entrer votre email.")
        
        user_obj = self.model(email=self.normalize_email(email),)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj
    
    def create_superuser(self, email, password, **extra_fields):
        user= self.create_user(email=email, password=password,)
        user.is_admin = True
        user.is_staff = True
        user.save()
        return user
class User(AbstractUser):

    username = None
    email = models.EmailField(unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects =  UserManager()
    
    def __str__(self):
        return self.email

class Contributor(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_contributor')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_contributor')
