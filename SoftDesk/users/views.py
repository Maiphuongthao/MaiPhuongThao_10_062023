from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Contributor
from .serializers import UserSerializer, ContributorSerializer
from rest_framework.permissions import AllowAny

class SignupViewset(viewsets.ModelViewSet):
    User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny)
    
class ContributorViewset(viewsets.ModelViewSet):
    Contributor.objects.all()
    serializer_class = ContributorSerializer

