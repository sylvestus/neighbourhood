from dataclasses import field, fields
from pyexpat import model
from .models import Profile,User,NeighbourHood,Bussiness,Post

from django import forms


class UprofileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio']

class NewHoodForm(forms.ModelForm):
    class Meta:
        model=NeighbourHood
        fields=['name','location','count','description','image']

class BusinessesForm(forms.ModelForm):
    class Meta:
        model=Bussiness
        exclude = ('user',)

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude = ('user',)
        
    
    


class newPost(forms.Form):

    title = forms.CharField(max_length=200)
    project_image = forms.ImageField() 
    description =forms.CharField(max_length=500)
    url=forms.CharField(max_length=200)

class UuserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required.')
    class Meta:
        model = User
        fields = ('username', 'email')