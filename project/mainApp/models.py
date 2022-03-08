from django.db import models
from django import forms
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.
class WebUser(models.Model):
    user_email=models.EmailField(max_length=250)
    password=forms.CharField(widget=forms.PasswordInput)
    user_type=models.CharField(max_length=100)
    contact_no=models.IntegerField()

    def __str__(self):
        return self.user_email

class BlogPosts(models.Model):
    blog_category=models.CharField(max_length=100)
    blog_title=models.CharField(max_length=200)
    blogAuthor=models.ForeignKey(WebUser,on_delete=models.CASCADE)
    blogContent=RichTextField()
    blog_image=models.ImageField(upload_to="uploads/")
    blog_date=models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
    