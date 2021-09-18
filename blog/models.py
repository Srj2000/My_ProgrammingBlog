from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from .managers import CustomManager

# Create your models here.
class Post(models.Model):
    p_id = models.AutoField(primary_key=True)
    
    p_title = models.CharField(max_length=50, default="")
    p_body = models.TextField()
    p_head1 = models.CharField(max_length=500, default="")
    p_chead1 = models.TextField()
    p_head2 = models.CharField(max_length=500, default="")
    p_chead2 = models.TextField()
    p_author = models.ForeignKey(User, on_delete=models.PROTECT)
    p_date = models.DateTimeField(auto_now=True)
    p_thumbnail = models.ImageField(upload_to='blog/images', default="")
    objects=CustomManager()

    def __str__(self):
        return self.p_title

class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    postsno = models.IntegerField(default=0)
    postcomment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)


class Contact(models.Model):
    user=models.ForeignKey(User,  on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    email=models.EmailField()
    contact=models.IntegerField()
    query=models.TextField()
    
    

    def __str__(self):
        return f' contact by {self.user}'

