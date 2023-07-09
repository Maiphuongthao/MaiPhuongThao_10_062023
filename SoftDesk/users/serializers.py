from .models import Contributor
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator, ValidationError
from rest_framework.fields import EmailField, CharField
from django.contrib.auth.hashers import make_password
from projects.models import Project

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    
    email = EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = CharField(required=True)
    last_name = CharField(required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_active',
            'user_contributor',
            'project_created_by',
            'issue_created_by',
            'issue_assigned_to',
            'user_comment',
        )
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create(
        email=validated_data['email'],
        first_name=validated_data['first_name'],
        last_name=validated_data['last_name'],
        password = make_password(validated_data['password']))
        user.save() 
        return user

class ContributorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = (
            'id',
            'user_id',
            'project_id',
        )