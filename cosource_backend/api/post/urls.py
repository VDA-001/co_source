from django.urls import path, include
from rest_framework.authtoken import views
from django.conf import settings
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'',views.PostViewSet)

urlpatterns = [
    path('create-post/<int:id>/',views.post, name='Post'),
    path('submit-video-response/<int:volunteer_id>/<int:post_id>/',views.SubmitVideo,name="SubmitVideo"),
    path('submit-detail-response/<int:volunteer_id>/<int:post_id>/',views.SubmitDetail,name="SubmitDetail"),
    path('',include(router.urls))
]