from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Doctor
from hospital.models import Hospital
from patient.models import Patient_Record,Appointment
# Create your views here.
def doctorclick_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request,'doctor/doctorclick.html')

def home(request):
    return render(request,'doctor/home.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('f_name')
        l_name=request.POST.get('l_name')
        city=request.POST.get('city')
        state=request.POST.get('state')
        street=request.POST.get('street')
        pincode=request.POST.get('pincode')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password1=request.POST.get('password1')
        specialization=request.POST.get('specialization')
        qualification=request.POST.get('qualification')
        hospital_name=request.POST.get('hospital')
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
        hospital=Hospital.objects.get(Name=hospital_name)
        doctor = Doctor(user = myuser,is_doctor =  True,F_Name=username,L_Name=l_name,Street=street,City=city,State=state,Pincode=pincode,Specialization=specialization,Qualification=qualification,Hospital=hospital)
        doctor.save()
        myuser.save()
        messages.success(request,"Your Doctor account has been successfully created")
        # print("Success")
        return redirect("home")
    else:
        hosp_list=Hospital.objects.all()
        print(hosp_list)
        params={'hosp_list':hosp_list}
        # print(params)
        return render(request,'doctor/signup.html',params)

def login_u(request):
    return render(request,'doctor/login.html')

def logout_u(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect("/doctor")

def loginpage(request):
    if request.method=="POST":
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:#means it exists
            if Doctor.objects.get(user = user).is_doctor:
                login(request,user)
                doc=Doctor.objects.get(user=user)
                records=Patient_Record.objects.filter(Doctor=doc)
                appointment=Appointment.objects.filter(Patient_Record__in=records)
                params={'doc':doc,'records':records,'appointments':appointment}
                messages.success(request,"Successfully Logged in")
                return render(request,'doctor/loginpage.html',params)
            else:
                messages.error(request,"Wrong credentials,Please try again !")
                return render(request,'doctor/login.html')
        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'doctor/login.html')
    else:
        messages.success(request,"You need to login to access this")
        return render(request,'doctor/login.html')
def home_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request,'doctor/index.html')
