from django.contrib import admin
from .models import CustomUser,Volunteer

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Volunteer)