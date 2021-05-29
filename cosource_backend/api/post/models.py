from django.db import models
from api.user.models import CustomUser

class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="media")
    description = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, default=None, null=True, blank=True)
    link = models.CharField(max_length=20, default=None, null=True, blank=True)
    country = models.CharField(max_length=30,default="India")
    region = models.CharField(max_length=30 ,default="South")
    date = models.DateTimeField(auto_now_add=True)
    assigned = models.BooleanField(null=True)
    validated=models.BooleanField(default=False)

    def _str_(self):
        return str(self.user)