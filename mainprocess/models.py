from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    idno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=40)
    username=models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.username



class Message(models.Model):
    mno=models.AutoField(primary_key=True)
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="Msender")
    receiver = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="Mreceiver")
    mess=models.CharField(max_length=2000,null='true')
    read=models.BooleanField(default=False)
    time=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
         return f"{self.sender} to {self.receiver} status {self.mess}"

class TestOptions(models.Model):
    
   
    qno=models.AutoField(primary_key=True)

    choice=models.CharField(max_length=20) 

    def __str__(self):
         return f"{self.choice}"

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

