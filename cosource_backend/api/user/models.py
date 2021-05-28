from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager

class CustomUser(AbstractUser):
    name = models.CharField(max_length=50, default='Anonymous')
    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=254, unique=True)
    session_token = models.CharField(max_length=10,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=15,blank = True,null=True)
    is_volunteer = models.BooleanField()
    country = models.CharField(max_length=30,null=False)
    region = models.CharField(max_length=30,null=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []