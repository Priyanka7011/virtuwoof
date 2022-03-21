from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('create',views.createPost,name='createPost'),
    path('display',views.displayPosts,name='displayPost'),
    path('delete',views.deletePost,name='deletePost'),
    path('geoapi',views.geoapify,name='geoapi'),
    path('new',views.newPost,name='newPost'),
]