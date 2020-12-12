from django.shortcuts import render,redirect
from django .http import HttpResponse
from doctor.models import Doctor
from patient.models import Patient,Patient_Record,Appointment
def home(request):
    return render(request,'health/home.html')

def aboutus_view(request):
    return render(request,'health/aboutus.html')

def contactus_view(request):
    return render(request,'health/contactus.html')
def seedocs(request):
    # SELECT CONCAT_WS(' ','Dr.',F_Name,L_Name) AS Name,Qualification,Specialization,CONCAT_WS(',',Street,City,State,Pincode) AS Address,Phone_no,AVG(Appointments.Ratings)AS Ratings,COUNT(Phone_no) AS Number_Of_Ratings FROM Doctor
    # INNER JOIN Patient_Records
    # ON Doctor.Id=Patient_Records.Doctor_Id
    # INNER JOIN Appointments
    # ON Patient_Records.Id=Appointments.Patient_Records_Id
    # WHERE Doctor.Specialization='Cardiologist'
    # GROUP BY Name;

    category=Doctor.objects.all().order_by('Specialization')
    alldocs=[]
    for cat in category:
        records=Patient_Record.objects.filter(Doctor=cat)
        appointment=Appointment.objects.filter(Patient_Record__in=records)
        # jash=sum(appointment.Ratings)/len(appointment.Ratings)
        # # print(jash)
        # print(len(appointment))
        sum=0
        for app in appointment:
            sum+=app.Ratings
        if len(appointment)==0:
            avg=0;
        else:
            avg=round(sum/len(appointment),2)
        alldocs.append([cat,avg,len(appointment)])
        alldocs.sort(key = lambda x: x[1],reverse=True)
        alldocs.sort(key = lambda x: x[0].Specialization)

    params={'category':alldocs}
    return render(request,'health/seedocs.html',params)
