# from django.shortcuts import render
import string

import jwt
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator
from MyAPI.models import MyUser, Video
from MyAPI.serializers import (RegistrationSerializer, UserSerializer,
                               VideoSerializer)
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *

# login = './User/login.html'
# home_page = './User/home.html'


# def base(request):
#     return render(request,'base.html')


class Register(TokenObtainPairView):
    serializer_class = RegistrationSerializer
    def post(self, request):         # creer user
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        pseudo = request.data.get('pseudo')
        if not username:
            return Response({
                'message': 'Error',
                'data': {'error': 'Username is required'}
            }, status=status.HTTP_400_BAD_REQUEST)
        user = MyUser(username=username, email=email, pseudo=pseudo, password=password)
        user.set_password(password)
        user.save()
        user_data = RegistrationSerializer(user).data
        return Response({'message': 'Ok','data': user_data}, status=status.HTTP_201_CREATED)
    
    
class GetUsers(TokenObtainPairView,):
    serializer_class = RegistrationSerializer
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

# @parser_classes([JSONParser])
class Login(TokenObtainPairView):
    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)
        if (user is not None) :  
            request.session['id'] = user.id
            login(request, user)
            payload = {
            'id': request.user.id,
            'username': request.user.username
            }
            jwt_token = jwt.encode(payload, '1999', algorithm='HS256')
            # salah = jwt.decode(request.jwt_token, 'your_secret_key', algorithms=['HS256'])
            

            return Response({'message': "OK",'data': jwt_token})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        

class Users(TokenObtainPairView):
    # permission_classes = [IsAuthenticated]
    serializer_class = RegistrationSerializer
    def get(self, request, id):
        try:
            user = MyUser.objects.get(pk=id)
            serializer = RegistrationSerializer(user)
            return Response({
                'message': 'Ok',
                'data': serializer.data
            }, status=status.HTTP_200_OK)              
        except MyUser.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
    # def delete(self, request):    # Login user
    #     logout(request)
    #     return Response({'Message': 'User logged out successfully'})
    
    def delete(self, request, id, format=None):
        print(id)
        user = MyUser.objects.get(id=id)
        user.delete()
        logout(request)
        return Response({'Message': 'Your account deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, id):     # Update user
        # id = request.session.get('id')
        user = MyUser.objects.get(id=id)
        serializer = RegistrationSerializer(user, data=request.data, partial=True)
        # id = request.data.get(id)
        admin = MyUser.objects.get(id=id)
        get = UserSerializer(user, data=request.data, partial=True)
        if (serializer.is_valid()):
            serializer.save()
            return Response({'message': "OK",'data': serializer.data}, status=status.HTTP_200_OK)
        elif (get.is_valid()) and (user.is_staff):
            get.save()
            return Response({'Message': 'User Update successfully  ', "Users Data":serializer.data })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateVideoView(TokenObtainPairView):
    serializer_class = VideoSerializer

    def post(self, request, id):
        user = MyUser.objects.get(id=id)
        name = request.data.get('name')
        source = request.FILES.get('source')  # Use FILES to handle uploaded files

        if not name or not source:
            return Response({'Message': 'Name and source file are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Save the file using FileSystemStorage
        fs = FileSystemStorage()
        filename = fs.save(source.name, source)

        # Create the video object
        video = Video.objects.create(name=name, source=filename, UserID=user)
        return Response({'message': 'OK', 'data': VideoSerializer(video).data}, status=status.HTTP_201_CREATED)

class GetVideos(TokenObtainPairView):
    serializer_class = VideoSerializer

    def get(self, request):
        name = request.query_params.get('name', None)
        page = request.query_params.get('page', 1)
        perPage = request.query_params.get('perPage', 5)

        videos = Video.objects.all().order_by('-id')  # Ensure explicit ordering

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

class ManageMyVideo(TokenObtainPairView):
    serializer_class = VideoSerializer

    def get(self, request, id):
        page = request.query_params.get('page', 1)
        perPage = request.query_params.get('perPage', 5)
        if id is not None:
            user = MyUser.objects.get(id=id)
            if not user.is_staff :
                video = Video.objects.filter(UserID = user)
                paginator = Paginator(video, perPage)
                page_obj = paginator.get_page(page)
                serializer = VideoSerializer(page_obj, many=True)
                return Response({
                                "message": "OK",
                                "data": serializer.data,
                                "pager": {
                                    "current": page_obj.number,
                                    "total": paginator.num_pages
                                }
                            }, status=status.HTTP_200_OK)
            else:
                video = Video.objects.all().values()
                paginator = Paginator(video, perPage)
                page_obj = paginator.get_page(page)
                serializer = VideoSerializer(page_obj, many=True)
                return Response({
                                "message": "OK",
                                "data": serializer.data,
                                "pager": {
                                    "current": page_obj.number,
                                    "total": paginator.num_pages
                                }
                            }, status=status.HTTP_200_OK)
        else:
            return Response({'Message': 'You are not authorized to access this page'})

    
    
class GetVideo(TokenObtainPairView):
    serializer_class = VideoSerializer

    def get(self, request, id):
        video = Video.objects.get(pk=id)
        serializer = VideoSerializer(video)
        return Response({
            "message": "OK",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)
        
    def put(self, request, id):
        video = Video.objects.get(id=id)
        serializer = VideoSerializer(video, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': "OK",'data': serializer.data}, status=status.HTTP_200_OK)
        
    def delete(self, request, id):   
        video = Video.objects.get(id=id)
        video.delete()
        return Response({'Message': 'Your Video deleted successfully'}, status=status.HTTP_204_NO_CONTENT)