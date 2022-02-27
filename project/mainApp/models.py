from django.db import models
from django import forms
from djrichtextfield.models from RichTextField
# Create your models here.
class User(models.Model):
    user_email=models.EmailField(max_length=250)
    password=forms.CharField(widget=forms.PasswordInput)
    user_type=models.CharField(max_length=100)
    contact_no=models.IntegerField()

class BlogPosts(models.Model):
    blog_category=models.CharField(max_length=100)
    blogAuthor=models.OneToMany(User)
    blogContent=RichTextField()
    blog_reactions=models.ManyToMany(BlogReactions)

class BlogReactions(models.Model):
    reaction_type=models.CharField(max_length=100)
    blog_post=models.ManyToMany(BlogPosts)
    user=models.OneToMany(User)

class Transaction(models.Model):
    from_transaction=models.CharField(max_length=200)
    to_transaction=models.CharField(max_length=200)
    date=models.DateField()
    mode_of_payment=models.CharField(max_length=200)

