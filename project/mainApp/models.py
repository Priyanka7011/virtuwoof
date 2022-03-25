from django.db import models
from django import forms
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class WebUser(models.Model):
    user_email=models.EmailField(max_length=250)
    user_name=models.CharField(max_length=100,default="")
    password=forms.CharField(widget=forms.PasswordInput)
    user_type=models.CharField(max_length=100)
    contact_no=models.IntegerField()

    def __str__(self):
        return self.user_name

class BlogPosts(models.Model):
    blog_category=models.CharField(max_length=100)
    blog_title=models.CharField(max_length=200)
    blogAuthor=models.ForeignKey(User,on_delete=models.CASCADE)
    blogContent=RichTextField()
    blog_image=models.ImageField(upload_to="uploads/")
    blog_date=models.DateField(default=timezone.now)


    def __str__(self):
        return self.blog_title

class postActions(models.Model):
    actor=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(BlogPosts,on_delete=models.CASCADE)
    action_type= models.CharField(max_length=100)

    def __str__(self):
        return self.post.blog_title+"_"+self.action_type

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return self.user.username