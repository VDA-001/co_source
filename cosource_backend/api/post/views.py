from .models import Post
from django.http import JsonResponse
from api.user.models import CustomUser,Volunteer
from api.post.models import Post,PostStatusModel
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
        user_ = get_object_or_404(CustomUser,pk=id)

        post_obj=Post(
            user=user_,
            image=image_,
            description=description_,
            phone=phone_,
            link=link_,
            country=country_,
            region=region_,
        )
        post_obj.save()
        return JsonResponse({'success':'Successfully created the post'})
    else:
        return JsonResponse({'error':'Accepting only POST request'})

@csrf_exempt
def SubmitVideo(request,volunteer_id,post_id):
    if (request.method!='POST'):
        return JsonResponse({'error':'Accepting only POST request'})
    video_ = request.FILES.get('video','')
    volunteer_ = get_object_or_404(Volunteer,pk=volunteer_id)
    volunteer_.credit+=200
    volunteer_.save()
    post_ = get_object_or_404(Post,pk=post_id)
    post_.validated = True
    post_.accepted = True
    post_.save()
    instance = PostStatusModel(
        video=video_,
        volunteer=volunteer_,
        post=post_
    )
    instance.save()
    return JsonResponse({'success':'Successfully submitted video'})

@csrf_exempt
def SubmitDetail(request,volunteer_id,post_id):
    if(request.method!='POST'):
        return JsonResponse({'error':'Accepting only POST request'})
    detail_ = request.POST.get('detail')
    volunteer_ = get_object_or_404(Volunteer,pk=volunteer_id)
    volunteer_.credit+=200
    volunteer_.save()
    post_ = get_object_or_404(Post,pk=post_id)
    post_.validated = True
    post_.accepted = False
    post_.save()
    instance = PostStatusModel(
        detail=detail_,
        volunteer=volunteer_,
        post=post_
    )
    instance.save()
    return JsonResponse({'success':'Successfully submitted your response'})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer