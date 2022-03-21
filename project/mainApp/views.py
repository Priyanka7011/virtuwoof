from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import BlogForm
from .models import BlogPosts
import requests


def createPost(request):
    user=request.user
    if request.POST:
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            post=form.save(commit=False)
            post.blogAuthor=user
            post.save()
        
    return HttpResponse("hello")

def newPost(request):
    form=BlogForm()
    return render(request,"createPost.html",{'form':form})
def displayPosts(request):
    posts=BlogPosts.objects.all()
    print(posts)
    return render(request,"Allposts.html",{'posts':posts})

def deletePost(request,id):
    user=request.user
    post=get_object_or_404(BlogPosts,id=id)
    if request.method=='POST':
        post.delete()
        return HttpResponseRedirect("/")

    return HttpResponse("deleted")


def geoapify(request):
    geocode=requests.get("https://api.geoapify.com/v1/geocode/search?text=38%20Upper%20Montagu%20Street%2C%20Westminster%20W1H%201LJ%2C%20United%20Kingdom&apiKey=c3d5be4813bc4019b4fb4c9a71cfee88").json()
    
    longitude=str(geocode['features'][0]['properties']['lon'])
    latitude=str(geocode['features'][0]['properties']['lat'])
    print(longitude,latitude)

    placesApi=requests.get("https://api.geoapify.com/v2/places?categories=pet.veterinary&pet.service+pet.shop&filter=circle%3A"+longitude+"%2C"+latitude+"%2C5000&limit=20&apiKey=c3d5be4813bc4019b4fb4c9a71cfee88").json()
    #print((placesApi['features']))

    #print(placesApi['features'][10]['properties']['address_line1'])

    
    for i in range(len(placesApi['features'])):
        print(placesApi['features'][i]['properties']['address_line1'],",",placesApi['features'][i]['properties']['address_line2'])

    

        



    

    return HttpResponse("success")

        
def index(request):
    return render(request,'index.html')