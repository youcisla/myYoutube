"""
URL configuration for Django project.

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
from django.urls import path
from MyAPI import views
from MyAPI.views import Users


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', views.Register.as_view()),
    path('users', views.GetUsers.as_view()),
    path('auth', views.Login.as_view()),
    path('user/<int:id>', views.Users.as_view()),
    path('user/<int:id>/video', views.CreateVideoView.as_view()),
    path('videos', views.GetVideos.as_view()),
    path('user/<int:id>/videos', views.ManageMyVideo.as_view()),
    path('video/<int:id>', views.GetVideo.as_view()),
    
]

