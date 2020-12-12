from django.shortcuts import render,redirect
from django .http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Patient,Patient_Record,Appointment
from datetime import date
from doctor.models import Doctor
# Create your views here.
def patientclick_view(request):
    return render(request,'patient/patientclick.html')

def home(request):
    return render(request,'patient/home.html')

def signup(request):
    if request.method=="POST":
        username=request.POST.get('f_name')
        m_name=request.POST.get('m_name')
        l_name=request.POST.get('l_name')
        city=request.POST.get('city')
        state=request.POST.get('state')
        street=request.POST.get('street')
        pincode=request.POST.get('pincode')
        phonenumber=request.POST.get('phonenumber')
        dob=request.POST.get('dob')
        print(dob)
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
            print(password)
            messages.error(request,"Both passwords dont match")
            return redirect('signup')
        myuser=User.objects.create_user(username,email,password)
        patient = Patient(user = myuser,is_patient =  True,F_Name=username,M_Name=m_name,L_Name=l_name,Phone_No=phonenumber,DOB=dob,Street=street,City=city,State=state,Pincode=pincode)
        patient.save()
        myuser.save()
        messages.success(request,"Your Patient account has been successfully created")
        return redirect('/patient')
    else:
        return render(request,'patient/signup.html')

def login_u(request):
    return render(request,'patient/login.html')

def logout_u(request):
    logout(request)
    messages.success(request,'Successfully logged out')
    return redirect("/patient")

def loginpage(request):
    if request.method=="POST":
        loginusername=request.POST.get('loginusername')
        loginpassword=request.POST.get('loginpassword')
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:#means it exists
            if Patient.objects.get(user = user).is_patient:
                login(request,user)
                pat=Patient.objects.get(user=user)
                today = date.today()
                age = today.year - pat.DOB.year
                records=Patient_Record.objects.filter(Patient=pat)
                appointment=Appointment.objects.filter(Patient_Record__in=records)
                params={'patient':pat,'age':age,'records':records,'appointments':appointment}
                messages.success(request,"Successfully Logged in")
                return render(request,'patient/loginpage.html',params)
            else:
                messages.error(request,"Wrong credentials,Please try again !")
                return render(request,'patient/login.html')
        else:
            messages.error(request,"Wrong credentials,Please try again !")
            return render(request,'patient/login.html')
    else:
        messages.success(request,"You need to login to access this")
        return render(request,'patient/login.html')

def home_view(request):
    #if request.user.is_authenticated:
        #return HttpResponseRedirect('afterlogin')
    return render(request,'patient/index.html')
def record(request):
        if request.method=="POST" and request.user is not None:
            pat=Patient.objects.get(user=request.user)
            doc_name=str(request.POST.get('doctor')).split('(')[0]
            Name=doc_name+str(pat.F_Name)
            Diagnostics=request.POST.get('diagnostics')
            doctor=Doctor.objects.get(F_Name=doc_name)
            record = Patient_Record(Name=Name,Doctor=doctor,Patient=pat,P_Diagnostics=Diagnostics)
            record.save()
            messages.success(request,"Record Created Successfully")
            return redirect("/patient/loginpage")
        else:
            doc_list=Doctor.objects.all()
            params={'doc_list':doc_list}
            return render(request,'patient/record.html',params)
def appointment(request):
        if request.method=="POST" and request.user is not None:
            rec_name=request.POST.get('record')
            rec=Patient_Record.objects.get(Name=rec_name)
            date=request.POST.get('date')
            medication=request.POST.get('medication')
            medicines=request.POST.get('medicines')
            fee_paid=request.POST.get('fee')
            rating=request.POST.get('rating')
            app=Appointment(Patient_Record=rec,Date_Of_Appointment=date,Medicines=medicines,Medication=medication,Ratings=rating,Fee_Paid=fee_paid)
            app.save()
            messages.success(request,"Appointment Created Successfully")
            return redirect("/patient/loginpage")
        else:
            pat=Patient.objects.get(user=request.user)
            rec=Patient_Record.objects.filter(Patient=pat)
            params={'records':rec}
            return render(request,'patient/appointment.html',params)
