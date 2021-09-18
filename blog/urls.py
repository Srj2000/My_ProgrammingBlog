from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='blog'),
    path("aboutpost/<int:myid>/", views.aboutpost, name='aboutpost'),
    path("postcom/", views.postcom, name='postcom'),
    path("postblog/", views.postblog, name='postblog'),
     path("mypost/", views.mypost, name='mypost'),
    path("contact/", views.contact, name='contact'),
    path("search/", views.search, name='search'),
    path("signup/", views.signup, name='signup'),
    path("loginform/", views.handlelogin, name='handlelogin'),
    path("handlelogout/", views.handlelogout, name='handlelogout'),



]
