from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from .views import (CommentCreateView, CommentListView, UserCreateView,
                    UserDetailView, UserListView, VideoCreateView,
                    VideoDeleteView, VideoEncodeView, VideoListByUserView,
                    VideoListView, VideoUpdateView)

urlpatterns = [
    path('user', UserCreateView.as_view(), name='user-create'),
    path('auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/<int:id>', UserDetailView.as_view(), name='user-detail'),
    path('users', UserListView.as_view(), name='user-list'),
    # path('videos/create/', VideoCreateView.as_view(), name='video-create'),
    path('videos/', VideoCreateView.as_view(), name='video-create'),  # Supports POST
    path('videos/list/', VideoListView.as_view(), name='video-list'),  # Supports GET
    
    path('user/<int:id>/videos', VideoListByUserView.as_view(), name='video-list-by-user'),
    
    path('video/<int:id>/encode', VideoEncodeView.as_view(), name='video-encode'),  
    path('video/<int:id>', VideoUpdateView.as_view(), name='video-update'),
    path('video/<int:id>/delete', VideoDeleteView.as_view(), name='video-delete'),

    path('video/<int:id>/comment', CommentCreateView.as_view(), name='comment-create'),
    path('video/<int:id>/comments', CommentListView.as_view(), name='comment-list'),
]
