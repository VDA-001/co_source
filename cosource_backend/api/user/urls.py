from django.urls import path, include
from rest_framework.authtoken import views
from django.conf import settings
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'volunteer',views.VolunteerViewSet)
router.register(r'',views.UserViewSet)

urlpatterns = [
    path('login/',views.signin, name='signin'),
    path('logout/<int:id>/',views.signout,name='signout'),
    path('create-volunteer/<int:user_id>/',views.createVolunteer,name="createVolunteer"),
    path('assign-post/<int:volunteer_id>/<int:post_id>/',views.assignPostToVolunteer,name="AssignPost"),
    path('',include(router.urls))
]