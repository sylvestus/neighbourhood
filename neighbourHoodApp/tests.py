from django.test import TestCase

import datetime
from .models import Bussiness, NeighbourHood, Post, Profile 
from django.contrib.auth.models import User
from django.test import TestCase

class ProfileTest(TestCase):
    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighbourhood =  NeighbourHood(neighbourhood_name = "silvano36", neighbourhood_location= "Nairobi", admin = self.user,neighbourhood_description='Home is best all the time', neighbourhood_photo="neighbourhood.jpg")
        self.neighbourhood.save()
        self.profile = Profile(id=11,id_no=34306488,email='testmail@gmail.com', profile_pic='profile.jpg', bio=' testing class',neighbourhood=self.neighbourhood,
                                    user=self.user)
      
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        testsaved = Profile.objects.all()
        self.assertFalse(len(testsaved) < 0)    

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)

class NeighbourhoodTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="silvano36", password="123456")
        self.user.save()
        self.neighbourhood =  NeighbourHood(neighbourhood_name = "silvano36", neighbourhood_location= "Nairobi", admin = self.user,neighbourhood_description='Home is best all the time', neighbourhood_photo="neighbourhood.jpg")
        self.neighbourhood.save()(neighbourhood_name = "Embakasi", neighbourhood_location= "Nairobi", admin = self.user,neighbourhood_description='Home is best all the time', neighbourhood_photo="neighbourhood.jpg")
        self.neighbourhood.save()
   
    def test_instance(self):
        self.assertTrue(isinstance(self.neighbourhood,NeighbourHood))

    def test_save_neighbourhood(self):
        self.neighbourhood.save_hood()
        neighbourhood = NeighbourHood.objects.all()
        self.assertTrue(len(neighbourhood) > 0)

    def test_delete_neighbourhood(self):
        self.neighbourhood.delete_hood()
        testsaved = NeighbourHood.objects.all()
        self.assertFalse(len(testsaved) > 0)

class BusinessTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighbourhood =  NeighbourHood(neighbourhood_name = "Donholm", neighbourhood_location= "Nairobi", admin = self.user,neighbourhood_description='Home is best all the time', neighbourhood_photo="neighbourhood.jpg")
        self.neighbourhood.save()
        self.bussiness = Bussiness(user=self.user,business_name="Business", business_neighbourhood=self.neighbourhood,business_email="testbusiness@gmail.com", business_description="Business test setup")
        self.bussiness.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.bussiness,Bussiness))

    def test_save_business(self):
        self.bussiness.save_business()
        bussiness = Bussiness.objects.all()
        self.assertTrue(len(bussiness) > 0)

    def test_delete_hood(self):
        self.bussiness.delete_business()
        bussiness = Bussiness.objects.all()
        self.assertFalse(len(bussiness) > 0)

class PostTest(TestCase): 

    def setUp(self):
     
        self.user = User(username="Test", password="testingpassword")
        self.user.save()
        self.neighbourhood =  NeighbourHood(neighbourhood_name = "Donholm", neighbourhood_location= "Nairobi", admin = self.user,neighbourhood_description='Home is best all the time', neighbourhood_photo="neighbourhood.jpg")
        self.neighbourhood.save()
        self.post = Post(user=self.user,title="User post",image="post.jpg" ,content ="user post", timestamp=datetime.datetime,neighbourhood=self.neighbourhood)
        self.post.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_post(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Post.objects.all()
        self.assertFalse(len(post) > 0)
