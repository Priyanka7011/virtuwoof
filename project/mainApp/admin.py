from django.contrib import admin

# Register your models here.
from mainApp.models import WebUser, BlogPosts,postActions,Profile,Helpline
admin.site.register(WebUser)
admin.site.register(BlogPosts)
admin.site.register(postActions)
admin.site.register(Profile)
admin.site.register(Helpline)

