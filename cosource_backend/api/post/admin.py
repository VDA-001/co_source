from django.contrib import admin
from .models import Post,PostStatusModel

# Register your models here.
admin.site.register(Post)
admin.site.register(PostStatusModel)