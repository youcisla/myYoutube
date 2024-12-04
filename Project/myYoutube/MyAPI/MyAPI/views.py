# from django.shortcuts import render
import string
from rest_framework. response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from django.contrib.auth import login, logout, authenticate
from MyAPI.serializers import  VideoSerializer, RegistrationSerializer, UserSerializer
from .models import *
from MyAPI.models import MyUser, Video
import jwt
from rest_framework.decorators import parser_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import JSONParser
from django.core.paginator import Paginator

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

    def post(self, request,id):
        print(id)
        if id is not None:
            name = request.data.get('name')
            source = request.data.get('source')
            UserID = MyUser.objects.get(id=id)
            if (not source) or (not name):
                return Response({'Message': 'name and file are required'})
            video = Video(name=name, source=source, UserID=UserID)
            video.save()
            video_data = VideoSerializer(video).data
            return Response({"message": "OK","data": video_data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'Message': 'Login before you create a Video'})



class GetVideos(TokenObtainPairView):
    serializer_class = VideoSerializer

    def get(self, request):
        video = Video.objects.all()
        name = request.query_params.get('name', None)
        user = request.query_params.get('user', None)
        duration = request.query_params.get('duration', None)
        page = request.query_params.get('page', 1)
        perPage = request.query_params.get('perPage', 5)
        if name:
            users = Video.objects.filter(username__icontains=name)  
        else:
            users = Video.objects.all()
        paginator = Paginator(users, perPage)
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