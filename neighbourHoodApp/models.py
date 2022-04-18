
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    count = models.IntegerField()
    description = models.TextField()
    image = CloudinaryField('images')
    admin=models.ForeignKey(User,on_delete=models.CASCADE, related_name='admin') 

    def __str__(self):
        return self.name

    
    def create_neigborhood(self):
        self.save()
    @classmethod
    def delete_neigborhood(cls,id):
        cls.objects.filter(id).delete()
    @classmethod
    def find_neigborhood(cls,searched_name):
        neigborhood = cls.objects.filter(name__icontains=searched_name)
        return neigborhood
    
    @classmethod
    def update_neighborhood(cls,id):
        cls.objects.filter(id=id).update()
        
    
    @classmethod
    def update_occupants(cls,id):
        cls.objects.filter(id=id).update()
        


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    id_no=models.IntegerField()
    neighborhood=models.ForeignKey(NeighbourHood, on_delete=models.CASCADE, blank=True, null=True)
    email=models.EmailField()
    profile_pic = CloudinaryField('profile')
    bio = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return self.user.username



    def save_profile(self):
        self.save()
        
    @classmethod
    def get_profile(cls,id):
        profile = Profile.objects.all()
        return profile
        
    @classmethod
    def update_profile(cls,id):
        cls.objects.get(user_id=id)

    @classmethod
    def delete_profile(cls,id):
        cls.objects.filter(id).delete()




class Bussiness(models.Model):
    name=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    neighborhood=models.ForeignKey(NeighbourHood,on_delete=models.CASCADE,blank=True,null=True)
    b_email=models.EmailField()
    business_description = models.TextField(blank=True)

    def __str__(self):
        return self.name


    def create_business(self):
        self.save()

    @classmethod
    def delete_business(cls,id):
        cls.objects.filter(id).delete()

    @classmethod
    def find_business(cls,searched_name):
        business = cls.objects.filter(name__icontains=searched_name)
        return business

    @classmethod
    def update_business(cls,id):
        cls.objects.filter(id=id).update()

class Post(models.Model):
    title = models.CharField(max_length=200)
    post_image = CloudinaryField('images')
    content =models.TextField()
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    profile=models.ForeignKey(Profile,on_delete= models.CASCADE,null=True)
    neighborhood=models.ForeignKey(NeighbourHood,on_delete= models.CASCADE,null=True)
    posted_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title


