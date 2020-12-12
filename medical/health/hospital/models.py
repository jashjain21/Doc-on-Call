from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Hospital(models.Model):
    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE,related_name="hospital")
    Id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=20)
    Street  = models.CharField(max_length=20)
    City  = models.CharField(max_length=20)
    State  = models.CharField(max_length=20)
    Pincode  = models.CharField(max_length=6)
    Phone_No =models.CharField(max_length=14)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default = False)
    is_hospital = models.BooleanField(default = False)
    def __str__(self):
        return self.Name
