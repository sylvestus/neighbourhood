from email import message
from urllib import request
from django.shortcuts import redirect, render
from .models import Post, User,Profile,Bussiness,NeighbourHood
from django.http.response import  HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .forms import PostForm,UprofileForm,UuserForm,NewHoodForm,BusinessesForm

# Create your views here.

def profile(request):
    current_user = request.user
    message='profile'
    # projects = Profile.objects.filter(user=current_user.id).all"projects": projects
    return render(request, 'profile.html', {'message':message })

def uprofile(request, id):
    current_user = request.user
    user_object = get_object_or_404(User, id=id)
    profile_object = get_object_or_404(Profile, user_id=id)
    profile_update = UprofileForm(request.POST or None ,request.FILES, instance=profile_object)
    user_update = UuserForm(request.POST or None, instance=user_object,)
    if profile_update.is_valid() and user_update.is_valid():
        user_update.save()
        profile_update.save()
        return HttpResponseRedirect("/showProfile")

    return render(
        request, "uprofile.html",{"profile_update": profile_update, "user_update": user_update})
def search_hood(request):
    if 'neighborhood' in request.GET and request.GET["neighborhood"]:
        search_term = request.GET.get("neighborhood")
        searched_neighborhoods = NeighbourHood.find_neigborhood(search_term)
        message = f"{search_term}"

        return render(request, 'searched.html',{"message":message,"searched_articles": searched_neighborhoods})

    else:
        message = "You haven't searched for any term"
    return render(request, 'searched.html',{"message":message})


def search_bizz(request):

    if 'bizz' in request.GET and request.GET["bizz"]:
        search_term = request.GET.get("bizz")
        searched_bussinesses = Bussiness.find_business(search_term)
        message = f"{search_term}"

        return render(request, 'searched.html',{"message":message,"searched_articles": searched_bussinesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'searched.html',{"message":message})

def home(request):
    message='welcome home'

    hoods= NeighbourHood.objects.all()

    return render(request,'home.html',{'message':message,'hoods':hoods})

def more(request,id):
    message='more page'
    more_onHood=NeighbourHood.objects.filter(id=id).get()
    current_hood=more_onHood.name
    busenesses=Bussiness.objects.filter(neighborhood=id)
    posts=Post.objects.filter(neighborhood=id)
    
 
    return render(request,'more.html',{'message':message,'hood':more_onHood ,'businesses':busenesses,'current_hood':current_hood,'posts':posts})

def deleteHood(request,id):
   
    deleteHood=NeighbourHood.objects.filter(id=id)
    deleteHood.delete()

    return redirect('home')

def new_hood(request):
    message='new neighbourhood'
    if request.method=="POST":
        current_user=request.user
        form = NewHoodForm(request.POST,request.FILES)
        if form.is_valid():
            name= form.cleaned_data["name"]
            location= form.cleaned_data["location"]
            count= form.cleaned_data["count"]
            description= form.cleaned_data["description"]
            image= form.cleaned_data['image']
            admin=current_user

            newHood=NeighbourHood(name=name,location=location,count=count,description=description,image=image,admin=admin)
            newHood.save()
        return redirect('home')
    else:
        form = NewHoodForm()
    return render(request,'newhood.html',{'message':message, 'newHoodForm':form})

def new_bizz(request):
    if request.method=="POST":
        current_user=request.user
        
        form=BusinessesForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.user = current_user
            business.save()
            
        return redirect('home')
           

    else:
        
        form = BusinessesForm
    return render(request,'newbizz.html',{'newbizz':form })

def deletebizz(request,id):
    deletebizz=Bussiness.objects.filter(id=id)
    deletebizz.delete()

    return redirect('home')

def new_post(request):
    if request.method=="POST":
        current_user=request.user
        
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            
        return redirect('home')
           

    else:
        
        form = PostForm
    return render(request,'newpost.html',{'newpost':form })

def deletepost(request,id):
    post=Post.objects.filter(id=id)
    post.delete()

    return redirect('home')








