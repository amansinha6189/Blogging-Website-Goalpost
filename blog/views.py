from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Blog, BlogComment
from blog.models import Contact
from blog.models import About

# Create your views here.
def home(request):
    return render(request, "home.html")
    
    

def blog(request):
    blogs = Blog.objects.all().order_by('-pk')
    context = {'blogs': blogs}
    return render(request, "blog.html", context)

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['content']
        # is_private = request.POST['is_private']
        # print(name, email, content)
        if len(name)<2 or len(email)<3 or len(content)<3:
            messages.error(request,"Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, content= content)
            contact.save()
            messages.success(request,"your message has been successfully sent")
    
    return render(request, "contact.html")



def search(request):
    query = request.GET['query']
    blogsTitle = Blog.objects.filter(title__icontains=query)
    blogsContent = Blog.objects.filter(content__icontains=query)
    blogs = blogsTitle.union(blogsContent)

    data1 = {'blogs': blogs, 'query':query}
    return render(request, "search.html", data1)

def about(request):
    abouts = About.objects.all()
    data2 = {'abouts':abouts}
    return render(request, "about.html", data2)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug)[0]
    comments = BlogComment.objects.filter(blog=blog)
    # print(blog)
    data = {'blog':blog, 'comments':comments}
    return render(request, "blogpost.html", data)

def blogComment(request):
    if request.method=="POST":
        comment = request.POST.get("comments")
        user = request.user
        blogSno = request.POST.get("blogSno")
        blog = Blog.objects.get(sno=blogSno)

        comment = BlogComment(comment=comment, user=user, blog=blog)
        comment.save()
        

        
    return redirect(f"/blog/{blog.slug}")


def handleSignup(request):
    if request.method=="POST":
        # get the post parameters
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        #check for errorneous inputs
        userCheck = User.objects.filter(username=username)

        if userCheck:
            messages.error(request, "Username Already taken")
            return redirect('/')

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request,"your account has been successfully created")
        return redirect('/')
    else:
        HttpResponse('404-not found')

def user_login(request):
    if request.method=="POST":
        user_name = request.POST.get('username', ' ')
        user_password = request.POST.get('password', ' ')
        
        #if user account exist or not
        user =  authenticate(username=user_name, password=user_password)

        if user is not None:
            login(request, user)
            messages.success(request, "logged in")
            return redirect('/')
        else:
            messages.error(request, "invalid credentials")
            return redirect('/')


def handleLogout(request):
    logout(request)
    messages.success(request,"Successfully logged out")
    return redirect("/")