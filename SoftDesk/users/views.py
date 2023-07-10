from django.contrib.auth import get_user_model
from rest_framework import viewsets, response, status
from rest_framework.permissions import IsAuthenticated, AllowAny


from .models import Contributor
from .permissions import ContributorPermisson
from .serializers import UserSerializer, ContributorSerializer
from projects.models import Project

User = get_user_model()


class SignupViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


class ContributorViewset(viewsets.ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [ContributorPermisson, IsAuthenticated]

    def get_queryset(self):
        contributors = Contributor.objects.filter(project_id=self.kwargs["project_pk"])
        return contributors

    def create(self, request, *args, **kwargs):
        # getting
        # https://stackoverflow.com/questions/68113403/assign-pk-form-url-to-models-related-field
        project_id = request.data["project_id"]
        project = Project.objects.filter(id=project_id).first()
        user_id = request.data["user_id"]
        user = User.objects.get(id=user_id)

        try:
            Contributor.objects.get(user_id=user, project_id=project)
            return response.Response(
                "Cet utilisateur existe deja.", status=status.HTTP_400_BAD_REQUEST
            )
        except Contributor.DoesNotExist:
            if user == project.author_user_id:
                return response.Response(
                    "l'author du project ne peut pas être contributor.",
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                serializer = ContributorSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return response.Response(
                        {"status": "success", "data": serializer.data},
                        status=status.HTTP_200_OK,
                    )
                else:
                    return response.Response(
                        {"status": "error", "data": serializer.errors},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
