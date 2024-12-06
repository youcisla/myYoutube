import os

import jwt
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from django.db import IntegrityError
from MyAPI.models import MyUser, Video
from MyAPI.serializers import (RegistrationSerializer, UserSerializer,
                               VideoSerializer)
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# MyAPI/views.py
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    """
    API endpoint for user login. Authenticates the user and returns an auth token.
    """
    def post(self, request):
        # Get username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # Generate or retrieve the token for the user
            token, created = Token.objects.get_or_create(user=user)
            
            return Response({
                "message": "Login successful",
                "token": token.key,
                "username": user.username
            }, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return Response({
                "message": "Invalid username or password"
            }, status=status.HTTP_401_UNAUTHORIZED)

class Register(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        pseudo = request.data.get('pseudo')

        if not username:
            return Response(
                {'message': 'Error', 'data': {'error': 'Username is required'}},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if the username already exists
        if MyUser.objects.filter(username=username).exists():
            return Response(
                {'message': 'Error', 'data': {'error': 'Username already taken'}},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = MyUser(username=username, email=email, pseudo=pseudo)
            user.set_password(password)
            user.save()
            user_data = RegistrationSerializer(user).data
            return Response({'message': 'Ok', 'data': user_data}, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response(
                {'message': 'Error', 'data': {'error': str(e)}},
                status=status.HTTP_400_BAD_REQUEST
            )

class CheckUsername(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        username = request.query_params.get('username')
        exists = MyUser.objects.filter(username=username).exists()
        return Response({'exists': exists}, status=status.HTTP_200_OK)

class Login(APIView):
    """
    View to handle user login and JWT token generation.
    """
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response(
                {"error": "Username and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            payload = {
                "id": user.id,
                "username": user.username,
            }
            jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
            return Response({"message": "OK", "data": jwt_token}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

class GetUsers(APIView):
    def get(self, request):
        pseudo = request.query_params.get('pseudo', None)
        page = request.query_params.get('page', 1)
        perPage = request.query_params.get('perPage', 5)

        if pseudo:
            users = MyUser.objects.filter(username__icontains=pseudo)
        else:
            users = MyUser.objects.all()

        paginator = Paginator(users, perPage)
        page_obj = paginator.get_page(page)
        serializer = RegistrationSerializer(page_obj, many=True)

        return Response({
            "message": "OK",
            "data": serializer.data,
            "pager": {
                "current": page_obj.number,
                "total": paginator.num_pages
            }
        }, status=status.HTTP_200_OK)


class Users(APIView):
    def get(self, request, id):
        try:
            user = MyUser.objects.get(pk=id)
            serializer = RegistrationSerializer(user)
            return Response({'message': 'Ok', 'data': serializer.data}, status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        user = MyUser.objects.get(pk=id)
        serializer = RegistrationSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Ok', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            user = MyUser.objects.get(pk=id)
            user.delete()
            return Response({'message': 'Your account deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except MyUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class CreateVideoView(APIView):
    def post(self, request, id):
        try:
            user = MyUser.objects.get(pk=id)
            name = request.data.get('name')
            source = request.FILES.get('source')

            if not name or not source:
                return Response({'message': 'Name and source file are required'}, status=status.HTTP_400_BAD_REQUEST)

            # Save the file
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save(source.name, source)

            # Create video object
            video = Video.objects.create(
                name=name,
                source=os.path.join('uploads', filename),
                UserID=user
            )

            return Response({
                'message': 'OK',
                'data': VideoSerializer(video, context={'request': request}).data
            }, status=status.HTTP_201_CREATED)
        except MyUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message': f'Error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetVideos(APIView):
    def get(self, request):
        name = request.query_params.get('name', None)
        page = request.query_params.get('page', 1)
        perPage = request.query_params.get('perPage', 5)

        videos = Video.objects.all().order_by('-id')

        if name:
            videos = videos.filter(name__icontains=name)

        paginator = Paginator(videos, perPage)
        page_obj = paginator.get_page(page)
        serializer = VideoSerializer(page_obj, many=True, context={'request': request})

        return Response({
            "message": "OK",
            "data": serializer.data,
            "pager": {
                "current": page_obj.number,
                "total": paginator.num_pages
            }
        }, status=status.HTTP_200_OK)


class ManageMyVideo(APIView):
    def get(self, request, id):
        try:
            user = MyUser.objects.get(pk=id)
            page = request.query_params.get('page', 1)
            perPage = request.query_params.get('perPage', 5)

            if not user.is_staff:
                videos = Video.objects.filter(UserID=user)
            else:
                videos = Video.objects.all()

            paginator = Paginator(videos, perPage)
            page_obj = paginator.get_page(page)
            serializer = VideoSerializer(page_obj, many=True, context={'request': request})

            return Response({
                "message": "OK",
                "data": serializer.data,
                "pager": {
                    "current": page_obj.number,
                    "total": paginator.num_pages
                }
            }, status=status.HTTP_200_OK)
        except MyUser.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)


class GetVideo(APIView):
    def get(self, request, id):
        try:
            video = Video.objects.get(pk=id)
            serializer = VideoSerializer(video, context={'request': request})
            return Response({
                "message": "OK",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        except Video.DoesNotExist:
            return Response({'message': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id):
        video = Video.objects.get(pk=id)
        serializer = VideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "OK", 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            video = Video.objects.get(pk=id)
            video.delete()
            return Response({'message': 'Your video deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        except Video.DoesNotExist:
            return Response({'message': 'Video not found'}, status=status.HTTP_404_NOT_FOUND)
