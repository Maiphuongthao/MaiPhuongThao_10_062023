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
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from users.views import SignupViewset, ContributorViewset
from projects.views import ProjectViewset
from rest_framework_nested import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'projects', ProjectViewset, basename='projects')


urlpatterns = router.urls

urlpatterns += [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-auth/", include('rest_framework.urls', namespace='rest_framework')),
    path("api/login/", TokenObtainPairView.as_view(), name='obtain_tokens'),
    path("api/token/refresh/", TokenRefreshView.as_view(), name='refresh_token'),
    path("api/signup/", SignupViewset.as_view({'post': 'create'}), name='signup'),
    
]