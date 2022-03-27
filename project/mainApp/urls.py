from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('services',views.services,name='services'),
    path('create',views.createPost,name='createPost'),
    path('display',views.displayPosts,name='displayPost'),
    path('delete',views.deletePost,name='deletePost'),
    path('geoapi',views.geoapify,name='geoapi'),
    path('new',views.newPost,name='newPost'),
    path('donate',views.donate,name='donate'),
    path('action',views.action,name='action'),
    path('allactions',views.allActionsList,name='allactions'),
    path('helpline',views.helpline,name='helpline'),
    path('chatbot',views.chat,name='chat'),
    path('checkout',views.checkout)
]