from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .forms import BlogForm,SearchForm
from .models import BlogPosts,postActions,Helpline
import requests


def services(request):
    return render(request,'services.html')

def createPost(request):
    user=request.user
    if request.POST:
        form = BlogForm(request.POST, request.FILES)
        
        if form.is_valid():
            post=form.save(commit=False)
            post.blogAuthor=user
            post.save()
        
    return HttpResponse("success")

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

    

def action(request):
    action_type=request.POST.get("action_btn")
    post_id=request.POST.get("post_id")
    print(action_type)
   
    
    blogpost=BlogPosts.objects.filter(id=post_id)[0]
    action_data=postActions(actor=request.user,post=blogpost,action_type=action_type)
    action_data.save()
    print(blogpost)

    if action_type=="Donation":
        return HttpResponseRedirect("/donate")
    

    return HttpResponse("success")

def allActionsList(request):
    user = request.user
    print(user)
    blogList=BlogPosts.objects.filter(blogAuthor=user)
    actionList=[]
    for blog in blogList:
        #print("shdhs")
        print(blog)
        actionList.append(postActions.objects.filter(post=blog))
    
    print(blogList)
    
    context_list=[]

    print(len(actionList))
    for i in range(len(actionList)):
        for action in actionList[i]:
            context_list.append(action)


    

    print(actionList)
    
    
    # for action in actionList:
    #     context_list.append(action)
    # print(context_list)
    
    return render(request,"Allactions.html",{"Blogpost":blogList,"actions":context_list})

def donate(request):
    return render(request,"donation.html")
def geoapify(request):

<<<<<<< HEAD
    if request.method=="POST":
=======
     if request.method=="POST":
>>>>>>> a64e961ced6f980a3fd595e9b502b083a5169b5a
        form = SearchForm(request.POST)
        if form.is_valid():
            address=form.cleaned_data['address']
            city=form.cleaned_data['city'] 
            state=form.cleaned_data['state']
            category=form.cleaned_data['filter_by']
            print(category)

        # address=request.POST.get("address")
        # city=request.POST.get("city")
        # state=request.POST.get("state")
        # category=request.POST.get("category")
        # print(category)
        full_addr=address+" "+city+" "+state
        addr_list=full_addr.split(" ")
        # print(addr_list)
        query_str=""
        for i in addr_list:
             query_str+=i+"%20"
        
        print(query_str)
        api="95a7c7bc64734406808395fa1d3139fb"
        geocode=requests.get("https://api.geoapify.com/v1/geocode/search?text="+query_str+"&apiKey=92ef0d6ee2ce46ceb9ae863be2aa7774").json()
        # #38%20Upper%20Montagu%20Street%2C%20Westminster%20W1H%201LJ%2C%20United%20Kingdom&apiKey=c3d5be4813bc4019b4fb4c9a71cfee88
        #geocode=requests.get("https://api.geoapify.com/v1/geocode/search?text=38%20Upper%20Montagu%20Street%2C%20Westminster%20W1H%201LJ%2C%20United%20Kingdom&apiKey=95a7c7bc64734406808395fa1d3139fb")

        print(geocode)
        
        
        longitude=str(geocode['features'][0]['properties']['lon'])
        latitude=str(geocode['features'][0]['properties']['lat'])
        print(longitude,latitude)

        placesApi=requests.get("https://api.geoapify.com/v2/places?categories="+category+"&filter=circle%3A"+longitude+"%2C"+latitude+"%2C5000&limit=20&apiKey=92ef0d6ee2ce46ceb9ae863be2aa7774").json()
        print((placesApi['features']))

        #print(placesApi['features'][10]['properties']['address_line1'])

        result=[]
        for i in range(len(placesApi['features'])):
            result.append(placesApi['features'][i]['properties'])

        print(result)

        isPresent=True

            



        form=SearchForm()

        return render(request,"search.html",{"form":form,"result":result,"isPresent":isPresent})
     form=SearchForm()
    
<<<<<<< HEAD
    form=SearchForm()
    
    return render(request,"search.html",{"form":form})
    

=======
     return render(request,"search.html",{"form":form})
>>>>>>> a64e961ced6f980a3fd595e9b502b083a5169b5a
    

def search(request):
    form=SearchForm()
    isPresent=False
    return render(request,"search.html",{"form":form,"isPresent":isPresent})

        
def index(request):
    return render(request,'index.html')

<<<<<<< HEAD
=======
def services(request):
    return render(request,'services.html')

>>>>>>> a64e961ced6f980a3fd595e9b502b083a5169b5a

        
def chat(request):
    return render(request,'chatbot.html')

def helpline(request):
    helplines=Helpline.objects.all()
    print(helplines)

    return render(request,'helpline.html',{"helplines":helplines})

def checkout(request):
     return render(request,'stripe.html')
<<<<<<< HEAD
=======


def map(request,lon,lat):
     #longitude=request.GET.get("lon")
     #latitude=request.GET.get('lat')
     print(lon,lat)
     url="https://maps.geoapify.com/v1/staticmap?style=osm-carto&width=700&height=400&center=lonlat:"+lon+","+lat+"&zoom=12&marker=lonlat:"+lon+","+lat+";color:%23ff0000;size:medium;text:1&apiKey=92ef0d6ee2ce46ceb9ae863be2aa7774"
     return render(request,'map.html',{"lon":lon,"lat":lat,"url":url})

>>>>>>> a64e961ced6f980a3fd595e9b502b083a5169b5a
