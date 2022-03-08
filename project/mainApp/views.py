from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import BlogForm
from .models import BlogPosts


def createPost(request):
    user=request.user
    if request.POST:
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.save()
        
    return HttpResponse("hello")

def displayPosts(request):
    posts=BlogPosts.object.all()
    return render(request,"Allposts.html",{'posts':posts})

def deletePost(request,id):
    user=request.user
    post=get_object_or_404(BlogPosts,id=id)
    if request.method=='POST':
        post.delete()
        return HttpResponseRedirect("/")

    return render(request)




        
def index(request):
    return HttpResponse('Hello Virtuwoof')