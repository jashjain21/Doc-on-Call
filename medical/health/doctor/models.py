from django.db import models
from django.contrib.auth.models import User
from hospital.models import Hospital

# class Belongs(models.Model):
#     user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="belong")
#     is_ngo = models.BooleanField(default=False)
#     is_donor = models.BooleanField(default = False)

# Create your models here.
# Create your models here.
class Doctor(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="doctor")
    Id = models.AutoField(primary_key=True)
    F_Name=models.CharField(max_length=20)
    L_Name =models.CharField(max_length=20)
    Street  = models.CharField(max_length=20)
    City  = models.CharField(max_length=20)
    State  = models.CharField(max_length=20)
    Pincode  = models.CharField(max_length=6)
    Qualification = models.CharField(max_length=20)
    Specialization = models.CharField(max_length=20)
    Hospital=models.ForeignKey(Hospital, on_delete=models.CASCADE,default=None,null=True)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default = False)
    is_hospital = models.BooleanField(default = False)
    def __str__(self):
        return self.F_Name
