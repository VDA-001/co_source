from rest_framework import serializers
from django.http import JsonResponse
from rest_framework.decorators import permission_classes
from .models import Post
from api.user.serializers import UserSerializer

class PostSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id','user','description','image','phone','link','country','region','assigned','validated')