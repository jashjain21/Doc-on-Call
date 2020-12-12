from django.db import models
from django.contrib.auth.models import User
from doctor.models import Doctor
# class Belongs(models.Model):
#     user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="belong")
#     is_ngo = models.BooleanField(default=False)
#     is_donor = models.BooleanField(default = False)

# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="patient")
    Id = models.AutoField(primary_key=True)
    F_Name=models.CharField(max_length=10)
    M_Name =models.CharField(max_length=10)
    L_Name =models.CharField(max_length=10)
    Phone_No =models.CharField(max_length=14)
    DOB = models.DateField(max_length=8)
    Street  = models.CharField(max_length=20)
    City  = models.CharField(max_length=20)
    State  = models.CharField(max_length=20)
    Pincode  = models.CharField(max_length=6)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default = False)
    is_hospital = models.BooleanField(default = False)
        #age  = models.IntegerField()
        # def __str__(self):
        #     today = date.today()
        #     age = today.year - dob.year
        #     if today.month < dob.month or today.month == dob.month and today.day < dob.day:
        #         age -= 1
        #     return self.age
        #
    def __str__(self):
        return self.F_Name
    class Meta:
        unique_together = ('F_Name', 'M_Name','L_Name')

class Patient_Record(models.Model):
    Id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=100,default=None,null=True)
    Patient = models.ForeignKey(Patient, on_delete=models.CASCADE,null=True)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,null=True)
    P_Diagnostics=models.CharField(max_length=20)
    def __str__(self):
        return self.Name
    class Meta:
        unique_together = ('Patient', 'Doctor')

class Appointment(models.Model):
    Id = models.AutoField(primary_key=True)
    Patient_Record = models.ForeignKey(Patient_Record, on_delete=models.CASCADE,null=True)
    Date_Of_Appointment = models.DateField(max_length=8)
    Medication = models.IntegerField()
    Medicines = models.CharField(max_length=200,default=None,null=True)
    Fee_Paid=models.DecimalField(max_digits=6, decimal_places=2)
    Ratings = models.IntegerField()
