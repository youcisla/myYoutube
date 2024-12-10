from django.contrib.auth.models import User
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


# Signal to create a token for every new user
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Connect the signal to the User model
post_save.connect(create_auth_token, sender=User)
