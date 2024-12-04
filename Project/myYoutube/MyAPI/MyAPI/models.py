from django.db import models
from django.contrib.auth.models import  AbstractUser



class MyUser(AbstractUser):
    id = models.IntegerField(primary_key=True)
    pseudo = models.CharField(max_length=20)
    # objects = CustomUserManager()

    groups = models.ManyToManyField(
        to='auth.Group',
        related_name='myapi_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        to='auth.Permission',
        related_name='myapi_users',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    USERNAME_FIELD = 'username'
    # EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    class Meta:
        db_table = "MyAPI"


class Video(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100) 
    source = models.FileField(upload_to='uploads/')
    UserID = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name