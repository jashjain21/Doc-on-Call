from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Hospital
from doctor.models import Doctor
# Create your views here.
def hospitalclick_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/hospitalclick.html')
def home(request):
    return render(request,'hospital/home.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('f_name')
        city=request.POST.get('city')
        state=request.POST.get('state')
        street=request.POST.get('street')
        pincode=request.POST.get('pincode')
        phonenumber=request.POST.get('phonenumber')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        if User.objects.filter(username=username).exists():
            messages.error(request,"Username already exists try with a new one !")
            return redirect('signup')
        if(len(username)<2 or len(username)>20):
            messages.error(request,"Username doesnt match the requirements")
            return redirect('signup')
        if not username.isalnum():
            messages.error(request,"Username must be alphanumeric")
            return redirect('signup')
        if(password!=password1):
            messages.error(request,"Both passwords dont match")
            return redirect('signup')
        myuser=User.objects.create_user(username,email,password)
        hospital = Hospital(user = myuser,is_hospital =  True,Name=username,Street=street,City=city,State=state,Pincode=pincode,Phone_No=phonenumber,)
        hospital.save()
        myuser.save()
        messages.success(request,"Your Hospital account has been successfully created")
        return redirect("home")
    else:
        return render(request,'hospital/signup.html')

def login_u(request):
    return render(request,'hospital/login.html')

def logout_u(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect("/hospital")

def loginpage(request):
    if request.method=="POST":
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:#means it exists
            if Hospital.objects.get(user = user).is_hospital:
                login(request,user)
                # print(user)
                # print(user.State)
                hosp=Hospital.objects.get(user=user)
                docs=Doctor.objects.filter(Hospital=hosp)
                print(docs)
                params={'hosp':hosp,'docs':docs}

                messages.success(request,"Successfully Logged in")
                return render(request,'hospital/loginpage.html',params)
            else:
                messages.error(request,"Wrong credentials,Please try again !")
                return render(request,'hospital/login.html')
        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'hospital/login.html')
    else:
        messages.success(request,"You need to login to access this")
        return render(request,'hospital/login.html')

def home_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request,'hospital/index.html')


#UPDATE BY NAITIK
