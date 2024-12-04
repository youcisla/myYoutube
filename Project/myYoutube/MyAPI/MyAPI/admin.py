from django.contrib import admin
from MyAPI import models
from MyAPI.models import MyUser
from MyAPI.models import Video
from django.contrib.auth.admin import UserAdmin
from django.db import models



class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'is_staff','pseudo')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'pseudo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

class VideoManager(admin.ModelAdmin):
    list_display = ('id', 'name', 'source', 'UserID')
    


admin.site.register(MyUser, CustomUserAdmin)
admin.site.register(Video, VideoManager)