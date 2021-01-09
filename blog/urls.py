"""goalpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog import views

admin.site.site_header = "Hi Lakshay!! Welcome to GoalPost"
admin.site.site_title = "Welcome to GoalPost "
admin.site.index_title = "Welcome to the Portal"

urlpatterns = [
    path('blog/blogComment/',views.blogComment, name='blogComment'),
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path("blog/blogpost/<str:slug>/", views.blogpost, name='blogpost'),
    path('search/', views.search, name='search'),
    path('signup/', views.handleSignup, name='handleSignup'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.handleLogout, name='handleLogout'),
    # Api to post a comment

]
