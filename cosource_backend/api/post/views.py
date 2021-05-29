from .models import Post
from django.http import JsonResponse
from api.user.models import CustomUser
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import PostSerializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def post(request,id):
    if(request.method=='POST'):
        image_= request.FILES.get('image','')
        description_ = request.POST.get('description')
        phone_ = request.POST.get('phone')
        link_ = request.POST.get('link')
        country_ = request.POST.get('country')
        region_ =request.POST.get('region')
        assigned_=request.POST.get('assigned')
        validated_ = request.POST.get('validated')
        user_ = get_object_or_404(CustomUser,pk=id)

        post_obj=Post(
            user=user_,
            image=image_,
            description=description_,
            phone=phone_,
            link=link_,
            country=country_,
            region=region_,
            validated=validated_,
            assigned=assigned_
        )
        post_obj.save()
        return JsonResponse({'success':'Created'})
    else:
        return JsonResponse({'error':'Accepting only POST request'})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer