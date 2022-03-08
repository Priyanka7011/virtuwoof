from django.contrib import admin

# Register your models here.
from mainApp.models import WebUser, BlogPosts
admin.site.register(WebUser)
admin.site.register(BlogPosts)
