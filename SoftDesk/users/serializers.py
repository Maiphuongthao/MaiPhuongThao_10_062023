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
        Model = User
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_active',
            'is_admin',
            'user_contributor',
            'project_created_by'
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
        field = (
            'id',
            'user_id',
            'project_id',
        )

    def validate_user(self, value):
        # get request user from serializer
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())
        if user == value:
            raise ValidationError("L'auteur du projet ne peut pas être contributeur")
        return value
    
    #write-operations to a nested serializer field :
   
    def create(self, validated_data):
        #getting
        #https://stackoverflow.com/questions/68113403/assign-pk-form-url-to-models-related-field
        p_id = self.context['view'].kwargs['pk']
        project = Project.objects.get(pk=p_id)

        contributor = Contributor.objects.create(
            user_id = validated_data['user'],
            project_id=project)
        return contributor