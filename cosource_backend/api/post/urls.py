from django.urls import path, include
from rest_framework.authtoken import views
from django.conf import settings
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'',views.PostViewSet)

urlpatterns = [
    path('create-post/<int:id>/',views.post, name='Post'),
    path('',include(router.urls))
]