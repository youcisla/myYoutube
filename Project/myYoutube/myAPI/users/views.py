import os

from django.contrib.auth import authenticate, get_user_model
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.settings import api_settings

from .models import Comment, Video
from .serializers import CommentSerializer, UserSerializer, VideoSerializer

User = get_user_model()

class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "Ok",
                "data": UserSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Bad Request",
            "code": 10001,
            "data": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def auth(request):
    login = request.data.get('login')
    password = request.data.get('password')

    user = authenticate(username=login, password=password)
    if user:
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({"message": "OK", "data": {"token": token}}, status=status.HTTP_201_CREATED)

class UserDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response({
            "message": "OK",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        data = request.data
        username = data.get("username")
        pseudo = data.get("pseudo")
        email = data.get("email")
        password = data.get("password")

        if username:
            user.username = username
        if pseudo:
            user.pseudo = pseudo
        if email:
            user.email = email
        if password:
            user.set_password(password)

        user.save()

        user_data = {
            "username": user.username,
            "pseudo": user.pseudo,
            "email": user.email,
        }

        return Response({"message": "Ok", "data": user_data}, status=status.HTTP_200_OK)

    def delete(self, request, id):
        try:
            user = User.objects.get(id=id)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

class UserListView(APIView):
    def get(self, request):
        pseudo = request.query_params.get('pseudo', None)
        page = request.query_params.get('page', 1)
        per_page = request.query_params.get('perPage', 10)

        if pseudo:
            users = User.objects.filter(pseudo__icontains=pseudo)
        else:
            users = User.objects.all()

        paginator = Paginator(users, per_page)
        current_page = paginator.get_page(page)
        serializer = UserSerializer(current_page, many=True)

        response_data = {
            "message": "OK",
            "data": serializer.data,
            "pager": {
                "current": current_page.number,
                "total": paginator.num_pages
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

class VideoCreateView(APIView):
    permission_classes = []  # Optional: Remove for public access
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            # Assign user if authenticated
            serializer.save(user=request.user if request.user.is_authenticated else None)
            return Response({"message": "Video created successfully", "data": serializer.data}, status=201)
        return Response({"errors": serializer.errors}, status=400)

class VideoListView(APIView):
    def get(self, request):
        name = request.query_params.get('name')
        user = request.query_params.get('user')
        duration = request.query_params.get('duration')
        page = int(request.query_params.get('page', 1))
        per_page = int(request.query_params.get('perPage', 10))

        videos = Video.objects.all()
        
        if name:
            videos = videos.filter(name__icontains=name)
        if user:
            videos = videos.filter(user__username=user) if isinstance(user, str) else videos.filter(user__id=user)
        if duration:
            videos = videos.filter(duration=duration)

        paginator = Paginator(videos, per_page)
        current_page = paginator.get_page(page)
        serializer = VideoSerializer(current_page, many=True)

        response_data = {
            "message": "OK",
            "data": serializer.data,
            "pager": {
                "current": current_page.number,
                "total": paginator.num_pages
            }
        }

        return Response({"message": "OK", "data": []}, status=status.HTTP_200_OK)

class VideoListByUserView(APIView):
    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except User.DoesNotExist:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        videos = Video.objects.filter(user=user)

        page_number = request.query_params.get('page', 1)
        per_page = request.query_params.get('perPage', 10)
        paginator = Paginator(videos, per_page)
        page_obj = paginator.get_page(page_number)

        serializer = VideoSerializer(page_obj, many=True)

        response_data = {
            "message": "OK",
            "data": serializer.data,
            "pager": {
                "current": page_obj.number,
                "total": paginator.num_pages
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

class VideoEncodeView(APIView):
    def patch(self, request, id):
        try:
            video = Video.objects.get(id=id)
        except Video.DoesNotExist:
            return Response({"detail": "Video not found"}, status=status.HTTP_404_NOT_FOUND)

        format = request.data.get("format")
        file = request.data.get("file")

        if format and file:
            video.source = f"encoded_{format}_{file}"
            video.save()
            return Response({
                "message": "OK",
                "data": VideoSerializer(video).data
            }, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

class VideoUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        try:
            video = Video.objects.get(id=id)
        except Video.DoesNotExist:
            return Response({"message": "Video not found"}, status=status.HTTP_404_NOT_FOUND)
        
        data = request.data
        video.name = data.get("name", video.name)
        
        user_id = data.get("user")
        if user_id:
            try:
                user = User.objects.get(id=user_id)
                video.user = user
            except User.DoesNotExist:
                return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        video.save()

        serializer = VideoSerializer(video)
        return Response({"message": "OK", "data": serializer.data}, status=status.HTTP_200_OK)

class VideoDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        video = get_object_or_404(Video, id=id)

        if video.source and os.path.exists(video.source.path):
            os.remove(video.source.path) 

        video.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        video = get_object_or_404(Video, id=id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(video=video, user=request.user)
            return Response({
                "message": "OK",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            "message": "Bad Request",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class CommentListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        video = get_object_or_404(Video, id=id)
        comments = Comment.objects.filter(video=video)
        
        page = request.query_params.get('page', 1)
        per_page = request.query_params.get('perPage', 10)
        paginator = Paginator(comments, per_page)
        current_page = paginator.get_page(page)
        
        serializer = CommentSerializer(current_page, many=True)
        
        response_data = {
            "message": "OK",
            "data": serializer.data,
            "pager": {
                "current": current_page.number,
                "total": paginator.num_pages
            }
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
        
class VideoCreateView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = []  # Allow unauthenticated users for now

    def post(self, request):
        # Provide a default user if request.user is not authenticated
        user = request.user if request.user.is_authenticated else None

        serializer = VideoSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            if user is None:  # Ensure user is set to avoid NOT NULL constraint errors
                return Response({
                    "message": "User must be logged in to upload a video."
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save(user=user)
            return Response({
                "message": "Video created successfully",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
            "message": "Bad Request",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
