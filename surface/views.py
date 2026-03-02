from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Contact

# Create your views here.
def surface(request):
    return render(request, "surface/startup.html")

def about(request):
    return render(request, "surface/about.html")

def portfolio(request):
    return render(request, "surface/portfolio.html")


def github(request):
    return redirect("https://www.github.com/novfensec")

def codepen(request):
    return redirect("https://www.codepen.io/novfensec")

def channel(request):
    return redirect("https://www.youtube.com/c/NovfensecInc/?sub_confirmation=1")

def stackoverflow(request):
    return redirect("https://stackoverflow.com/users/16486510/novfensec")

def contact(request):
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        if not name or not email or not phone or not message:
            messages.error(request, "Invalid response...")
        else:
            c = Contact(name=name, email=email, phone=phone, message=message)
            c.save()
            messages.success(request, "Your Response Has Been Recorded. I'll get back to you later.")
    return render(request,'surface/contact.html')

def errora(request,exception):
    context={'error':'404'}
    return render(request,'surface/error.html', context)
    
def errorb(request,exception):
    context={'error':'400'}
    return render(request,'surface/error.html', context)
    
def errorc(request,exception):
    context={'error':'403'}
    return render(request,'surface/error.html', context)
    
def errord(request,exception=None):
    context={'error':'500'}
    return render(request,'surface/error.html', context)

def handlrSignUp(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        # check for errorneous input
        if len(username)<3:
            messages.info(request, " Your user name must be under 3 characters")
            return redirect(request.META.get('HTTP_REFERER'))

        elif not username.isalnum():
            messages.info(request, " User name should only contain letters and numbers")
            return redirect(request.META.get('HTTP_REFERER'))
            
        elif (pass1!= pass2):
            messages.error(request, " Passwords do not match")
            return redirect(request.META.get('HTTP_REFERER'))
        
        elif User.objects.filter(username=username).exists():
            messages.info(request,"A user already exists with same Username. Please try another Username.")
            return redirect(request.META.get('HTTP_REFERER'))
        
        elif User.objects.filter(email=email).exists():
            messages.info(request,"A user already exists with same Email-Id. Please try another Email-Id.")
            return redirect(request.META.get('HTTP_REFERER'))
            
        else:
            myuser = User(username=username, email=email, first_name=fname, last_name=lname)
            myuser.set_password(pass1)
            myuser.save()
            user=authenticate(username= username, password= pass1)
            login(request, user)
            messages.success(request, " Your Account has been successfully created")
            return redirect(request.META.get('HTTP_REFERER'))

    else:
        if request.user.is_authenticated:
            return redirect("/")
        else:
            context={'signup':'current','display':True}
            return render(request, "surface/authenticate.html",context)
        
    return redirect(request.META.get('HTTP_REFERER'))

def handlrLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In.")
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        if request.user.is_authenticated:
            return redirect("/")
        else:
            context={'login':'current','display':False}
            return render(request, "surface/authenticate.html",context)

    return redirect("/")

def handlrLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out.")
    return redirect(request.META.get('HTTP_REFERER'))