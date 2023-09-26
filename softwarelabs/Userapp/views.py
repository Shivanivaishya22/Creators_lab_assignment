from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login, logout
from django.contrib import messages
from .models import Post
# from .models import Profile

# Create your views here.
def home(request):
    post = Post.objects.all()
    if request.method == "POST":
        caption = request.POST.get("caption")
        image = request.FILES.get("image")
        user = request.user
        user = Post(caption = caption , image = image , user= user)
        user.save()
        messages.success(request , "Post done Successfully")
        return render(request , "home.html", {"post": post})

    else:
        return render(request , "home.html", {})  

def Signup(request):
    if (request.method == "POST" ):
        uname = request.POST.get("uname")
        email = request.POST.get("email")
        pwd = request.POST.get("pwd")
        cpwd = request.POST.get("cpwd")
        checkuser = User.objects.filter(username = uname)
        if checkuser:
            messages.error(request , "User Already Exists" )
            return redirect (Signup)
        else:
            if ( pwd == cpwd):
                user = User.objects.create_user(username=uname , email = email , password = pwd)
                user.save()
                messages.success(request , f"User {uname} Created...")
                return redirect(Login) 
            else:
                messages.error(request , "Invalid Credentials")  
                return HttpResponse("Invalid") 

    else:
        return render (request , "signup.html",{})


def Login(request):
    if (request.method == "POST"):
          uname = request.POST.get("uname")
          pwd = request.POST.get("pwd")
          user = authenticate(username=uname , password=pwd)
          if (user is not None):
            login(request , user)
            messages.success(request , "Successfully Logged In....")
            return redirect(home)
          else:
              messages.error(request , "Invalid Credentials")  
              return redirect(Login)
    else:
        return render (request , "login.html" , {})

def Logout(request):
    logout(request)
    messages.success(request , "Succeesfully Logged Out")
    return redirect(home)
