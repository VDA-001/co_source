from django.db import models

class Post(models.Model):
    user = models.ForeignKey("user.CustomUser", on_delete=models.CASCADE)
    image=models.ImageField(upload_to="images/")
    description = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, default=None, null=True, blank=True)
    link = models.CharField(max_length=20, default=None, null=True, blank=True)
    country = models.CharField(max_length=30,default="India")
    region = models.CharField(max_length=30 ,default="South")
    date = models.DateTimeField(auto_now_add=True)
    assigned = models.BooleanField(default=False)
    validated=models.BooleanField(default=False)
    accepted=models.BooleanField(null=True)

    def _str_(self):
        return str(self.user)

class PostStatusModel(models.Model):
    detail = models.TextField(null=True)
    video = models.FileField(upload_to="videos/",null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    volunteer = models.ForeignKey("user.Volunteer", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)