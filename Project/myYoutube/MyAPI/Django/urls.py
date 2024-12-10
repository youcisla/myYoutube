from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from MyAPI import views
from MyAPI.views import AllVideosView, CreateVideoView, MyVideosView, Users
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('auth/check-username', views.CheckUsername.as_view(), name='check-username'),
    path("register/", views.Register.as_view(), name="register"),
    path('login/', views.LoginView.as_view(), name='login'),  # Use one definition
    path('user', views.Register.as_view()),
    path('users', views.GetUsers.as_view()),
    path('auth', views.Login.as_view()),  # Consider removing if unnecessary
    path('user/<int:id>', views.Users.as_view()),
    path('user/<int:id>/video', CreateVideoView.as_view(), name='create-video'),
    path('videos', views.GetVideos.as_view()),
    path('user/<int:id>/videos', views.ManageMyVideo.as_view()),
    path('video/<int:id>', views.GetVideo.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('my-videos/', MyVideosView.as_view(), name='my-videos'),
    path('all-videos/', AllVideosView.as_view(), name='all-videos'),
    path('upload-video/', views.UploadVideoView.as_view(), name='upload-video'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
