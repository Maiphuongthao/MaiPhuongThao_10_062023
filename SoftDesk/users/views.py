from django.contrib.auth import get_user_model
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Contributor
from .serializers import UserSerializer, ContributorSerializer
from rest_framework.permissions import AllowAny

User = get_user_model()
class SignupViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    
class ContributorViewset(viewsets.ModelViewSet):
    Contributor.objects.all()
    serializer_class = ContributorSerializer
    

