from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    return render(request, "index.html", {'username': request.user.username})

def shop(request):

    return render(request, "shop.html", {'username': request.user.username})

def shopdetail (request):

    return render(request,'shop-detail.html', {'username': request.user.username})

@login_required(login_url="login.html")
def cart(request):

    return render(request,'cart.html', {'username': request.user.username})

def chackout(request):

    return render(request,"chackout.html", {'username': request.user.username})

def testimonial(request):

    return render(request,'testimonial.html', {'username': request.user.username})

def four(request):
    return render(request,'404.html', {'username': request.user.username})

def contact(request):
    return render(request,'contact.html', {'username': request.user.username})

def error(request):
    return render(request,'404.html')

def login1(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get("uname")
        password = data.get("password")

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid credentials")
            return redirect("login.html")
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request, "Invalid credentials")
            return redirect("login.html")
        else:
            login(request, user)
            return redirect("cart.html")
        
    return render(request,'login.html', {'username': request.user.username})

def reg(request):
    if request.method=='POST':
        data = request.POST
        fname = data.get("fname")
        lname = data.get("lname")
        uname = data.get("uname")
        password = data.get("password")
        
        if User.objects.filter(username=uname).exists():
            messages.info(request,"Username exists !!!")
            return redirect("reg")

        else:
            user =  User.objects.create(first_name=fname,last_name=lname,username=uname)
            user.set_password(password)
            user.save()
            messages.info(request,"Registration successfully !!!")
            return redirect("reg")

    return render(request, 'registration.html')

def logoutpage(request):
    logout(request)
    return render(request,"login.html")