from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog/images', default="")
    content = models.TextField()
    slug = models.CharField(max_length=150)
    time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Contact(models.Model):
    sno =models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
    # phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=254)
    content = models.TextField()

    def __str__(self):
        return self.name+ "  |  "+ self.email
    


class About(models.Model):
    name = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='blog/images', default="")
    bio = models.CharField(max_length=150)
    para1 = models.TextField()
    para2 = models.TextField()
    para3 = models.TextField()

    def __str__(self):
        return self.name 

class Todo(models.Model):
    sno = models.AutoField(primary_key=True)
    task = models.CharField(max_length=150)
    description = models.TextField()
    priority = models.CharField(max_length=150)
    
    def __str__(self):
        return self.task

class BlogComment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)
    
