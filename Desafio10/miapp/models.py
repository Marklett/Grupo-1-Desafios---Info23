from django.db import models
from django.utils import timezone

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    registration_date = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    status = models.CharField(max_length=20, default='active')
    online = models.BooleanField(default=False)
    profile = models.CharField(max_length=11, default = 'Miembro')

    def __str__(self):
        return self.username

'''class Article(models.Model):
    id_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    resume = models.TextField()
    content = models.TextField()
    publication_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    status = models.CharField(max_length=20)

class Comments(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    articulo = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
'''