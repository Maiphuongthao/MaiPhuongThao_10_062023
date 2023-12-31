"""
URL configuration for SoftDesk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from users.views import SignupViewset, ContributorViewset
from projects.views import ProjectViewset
from issues.views import IssuesViewset
from comments.views import CommentViewset
from rest_framework_nested import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r"projects", ProjectViewset, basename="projects")

projects_router = routers.NestedDefaultRouter(router, r"projects", lookup="project")
projects_router.register(r"users", ContributorViewset, basename="users")

projects_router.register(r"issues", IssuesViewset, basename="issues")

issues_router = routers.NestedDefaultRouter(projects_router, r"issues", lookup="issue")
issues_router.register(r"comments", CommentViewset, basename="comments")


urlpatterns = router.urls

urlpatterns += [
    path("", include(projects_router.urls)),
    path("", include(issues_router.urls)),
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("login/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("token/refresh/", TokenRefreshView.as_view(), name="refresh_token"),
    path("signup/", SignupViewset.as_view({"post": "create"}), name="signup"),
]
