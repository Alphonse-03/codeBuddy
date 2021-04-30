from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

import uuid
from ckeditor.fields import RichTextField



class Profile(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    username=models.CharField(max_length=30,unique=True)
    dp = models.FileField(upload_to='dp/',default='/media/default.png')
    dplink = models.CharField(max_length=70,default='/media/default.png')
    
   
    def __str__(self):
        return self.username



class CustomUser(AbstractUser):
    is_recruiter=models.BooleanField(default=False)
    dp = models.FileField(upload_to='dp/',default='/media/default.png')
    dplink = models.CharField(max_length=70,default='/media/default.png')

class JobProfile(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    username=models.CharField(max_length=30,unique=True)
    
    def __str__(self):
         return f"{self.username} "


class JobPortal(models.Model):
    name=models.ForeignKey(JobProfile,on_delete=models.CASCADE,related_name="jobp")
    companyname=models.CharField(max_length=30)
    jTitle=models.CharField(blank=True,null=True,max_length=50)
    location=models.CharField(blank=True,null=True,max_length=30)
    noOfApplicants=models.CharField(blank=True,null=True,default=0,max_length=10)
    # jobDescription=models.TextField()
    jobDescription=RichTextField(blank=True,null=True)
  
    expectedSalary=models.CharField(max_length=20,blank=True,default="Declined to say")
    is_verified=models.BooleanField(default=False,blank=True)
    dp = models.FileField(upload_to='dp/',default='/media/default.png')
    dplink = models.CharField(max_length=70,default='/media/default.png')
    id = models.UUIDField(
         primary_key = True,
         default = uuid.uuid4,
         editable = False)

    def __str__(self):
         return f"from {self.companyname} "






class Applicants(models.Model):
    Applicants=models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="applicant")
    message=models.TextField(blank=True,null=True)
    ApplyingTo=models.ForeignKey(JobPortal, on_delete=models.CASCADE, related_name="JobPortal")
    resume = models.FileField(upload_to='documents/',null=True,blank=True)
    resumeli = models.CharField(max_length=70,null=True,blank=True)

    choice=(
        ("Accepted","Accepted"),
        ("Declined","Declined"),
        ("Pending","Pending")
    )

    status=models.CharField(max_length=10,choices=choice,blank=True)
    sender=models.BooleanField(default=True)
    def __str__(self):
         return f"{self.Applicants.username} applied at {self.ApplyingTo.companyname} status {self.status}"
    




class Message(models.Model):
    mno=models.AutoField(primary_key=True)
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="Msender")
    receiver = models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name="Mreceiver")
    # mess=models.CharField(max_length=2000,null='true')
    mess=RichTextField(blank=True,null=True)
    read=models.BooleanField(default=False)
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return f"{self.sender} to {self.receiver} status {self.mess}"






         

class TestOptions(models.Model):
    
   
    qno=models.AutoField(primary_key=True)

    choice=models.CharField(max_length=20) 

    def __str__(self):
         return f"{self.choice}"




class waste(models.Model):
    a=models.CharField(max_length=1,default=0)
    b=models.CharField(max_length=1,default=0)
    c=models.CharField(max_length=1,default=0)
    d=models.CharField(max_length=1,default=0)
    e=models.CharField(max_length=1,default=0)
    f=models.CharField(max_length=1,default=0)
    g=models.CharField(max_length=1,default=0)
    h=models.CharField(max_length=1,default=0)
    i=models.CharField(max_length=1,default=0)
    j=models.CharField(max_length=1,default=0)
    sub=models.ForeignKey(TestOptions, on_delete=models.CASCADE, related_name="Tesst")


class questions(models.Model):
    
    idno = models.AutoField(primary_key=True)
    Subject = models.ForeignKey(TestOptions, on_delete=models.CASCADE, related_name="Test")
    question=models.TextField()
    option1=models.CharField(max_length=100,null='true')
    option2=models.CharField(max_length=100,null='true')
    option3=models.CharField(max_length=100,null='true')
    option4=models.CharField(max_length=100,null='true')

    choices = (
        ('1', "1"),
        ('2', "2"),
        ('3', "3"),
        ('4', "4"),
    )
    answer=models.CharField(max_length=1, choices=choices)
    def __str__(self):
        return f"{self.question[0:150]} ***in*** {self.Subject}" 


class Intrest(models.Model):
    #idno = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="uuser")
    Intrest = models.ForeignKey(TestOptions, on_delete=models.CASCADE, related_name="int")
    marks=models.IntegerField(default=0)
    choices = (
        ('Legendary', "Legendary"),
        ('Titan', "Titan"),
        ('Champion', "Champion"),
        ('Master', "Master"),
        ('Crystal', "Crystal"),
        ('Gold', "Gold"),
        ('Silver', "Silver"),
        ('Bronze', "Bronze"),
    )
    category=models.CharField(max_length=10,choices=choices,blank=True,null=True)
    time=models.DateTimeField(auto_now_add=True,editable=True)

    



    def __str__(self):
         return f"{self.user}  {self.Intrest} {self.time}"







class ConnectRequest(models.Model):
    idno = models.AutoField(primary_key=True)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="receiver")
    sub=models.ForeignKey(TestOptions,on_delete=models.CASCADE, related_name="sub",null='true')
    
    choice=(
        ("Accepted","Accepted"),
        ("Declined","Declined"),
        ("Pending","Pending")
    )

    status=models.CharField(max_length=10,choices=choice,blank=True)
    
    def __str__(self):
         return f"{self.sender} to {self.receiver} status {self.status} for {self.sub}"



