from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('more/<int:id>',views.more,name='more'),
    path('delete/<int:id>',views.deleteHood, name='deleteHood'),
    path('deletebizz/<int:id>',views.deletebizz, name='deletebizz'),
    path('deletepost/<int:id>',views.deletepost, name='deletepost'),
    path('newhood/',views.new_hood,name='new_hood'),  
    path('newbizz/',views.new_bizz,name='new_bizz'), 
    path('newpost/',views.new_post,name='new_post'), 
    path('profile/',views.profile,name='profile'),
    path('showProfile',views.profile,name='showProfile'),
    path('showProfile/update/<int:id>',views.uprofile,name='uprofile'),
    path('search/',views.search_hood,name='search'),
    path('search_bizz/',views.search_bizz,name='search_bizz'),
]