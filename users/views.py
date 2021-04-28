from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import questions,Profile,TestOptions,Intrest,Message,ConnectRequest,waste,JobProfile,JobPortal,Applicants
import random 
import datetime
from datetime import timedelta,date
from django.db.models import Q
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from .models import CustomUser
from .filters import ApplicantFilter
# Create your views here.
from django.core.files.storage import FileSystemStorage

def uploaddp(request):
    #person=Profile.objects.filter(username=request.user)
    if request.method == 'POST' and request.FILES['myfile']:

            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            Profile.objects.filter(username=request.user).update(dp=uploaded_file_url,dplink=uploaded_file_url)
            # jj.save()
            # applicantss=int(applicants)+1
            # JobPortal.objects.filter(id=slug).update(noOfApplicants=applicantss)
            # messages.success(request,"Applied Successfully")
  
            return redirect("profile")
    return render(request,"code/uploaddp.html")


def lresponse(request):
    person=Profile.objects.get(username=request.user)
    job=Applicants.objects.filter(Applicants=person).filter(sender=True).filter(status="Pending")
    return render(request,"code/lresponse.html",{'job':job})

def viewdetailaccept(request,slug):
    job=JobPortal.objects.get(id=slug)
    person=Profile.objects.get(username=request.user)
    Applicants.objects.filter(Applicants=person).filter(ApplyingTo=job).update(status="Accepted")

    return redirect("jrequest")

def viewdetail2(request,slug):
    job=JobPortal.objects.get(id=slug)
    return render(request,"code/viewdetail2.html",{'job':job}) 

    return redirect("jrequest")
def viewdetailreject(request,slug):
    job=JobPortal.objects.get(id=slug)
    person=Profile.objects.get(username=request.user)
    Applicants.objects.filter(Applicants=person).filter(ApplyingTo=job).update(status="Declined")
    return redirect("jrequest")

def notIntrested(request,slug):
    job=JobPortal.objects.get(id=slug)
    person=Profile.objects.get(username=request.user)
    Applicants.objects.filter(Applicants=person).filter(ApplyingTo=job).delete()
    return redirect("jrequest")

def viewdetail(request,slug):
    job=JobPortal.objects.get(id=slug)
    return render(request,"code/viewdetail.html",{'job':job}) 


def jrequest(request):
    person=Profile.objects.get(username=request.user)
    job=Applicants.objects.filter(Applicants=person).filter(sender=False).filter(status="Pending")
    return render(request,"code/jrequest.html",{'job':job})






def apply(request):
    job=JobPortal.objects.filter(is_verified=True)
    return render(request,"code/apply.html",{'jobs':job})

def applyto(request,slug):
    job=JobPortal.objects.get(id=slug)
    applicants=job.noOfApplicants
    person=Profile.objects.get(username=request.user)
    applied=False
    if Applicants.objects.filter(Applicants=person).filter(ApplyingTo=job).exists()==False:

        if request.method == 'POST' and request.FILES['myfile']:

            myfile = request.FILES['myfile']
            mess = request.POST['jd']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            jj=Applicants(Applicants=person,ApplyingTo=job,status="Pending",message=mess,resumeli=uploaded_file_url,resume=uploaded_file_url)
            jj.save()
            applicantss=int(applicants)+1
            JobPortal.objects.filter(id=slug).update(noOfApplicants=applicantss)
            messages.success(request,"Applied Successfully")
            applied=True
            return render(request,"code/applyto.html",{'job': job,'uploaded_file_url': uploaded_file_url,'applied':applied})
            
        
        return render(request,"code/applyto.html",{'job': job,'applied':applied})
    
    
    if Applicants.objects.filter(Applicants=person).filter(ApplyingTo=job).exists():

        messages.warning(request,"Already Applied")
        return redirect('apply')
    


        














def confirmedppl(request,slug):
    job=JobPortal.objects.get(id=slug)
    confirmedppl=Applicants.objects.filter(ApplyingTo=job).filter(status="Accepted")
    return render(request,"code/confirmedppl.html",{'confirmedppl':confirmedppl})






def acceptapplicant(request,slug,name):
    job=JobPortal.objects.get(id=slug)
    nam=Profile.objects.get(username=name)
    Applicants.objects.filter(Applicants=nam,ApplyingTo=job).update(status="Accepted")
    return redirect("seeapplicants",slug=slug)

def declineapplicant(request,slug,name):
    job=JobPortal.objects.get(id=slug)
    nam=Profile.objects.get(username=name)
    Applicants.objects.filter(Applicants=nam,ApplyingTo=job).update(status="Declined")
    return redirect("seeapplicants",slug=slug)


def addapplicant(request,slug,name):
    job=JobPortal.objects.get(id=slug)
    pro=Profile.objects.get(username=name)
    if len(Applicants.objects.filter(ApplyingTo=job,Applicants=pro))==0:
        s=Applicants(ApplyingTo=job,Applicants=pro,status="Pending",sender=False)
        s.save()
        messages.success(request,"Request has been send to the user")
    else:
        messages.warning(request,"Request has already been sent to the user")
    return redirect("findppl",slug=slug)


def seeapplicants(request,slug):
    job=JobPortal.objects.get(id=slug)
    ppl=Applicants.objects.filter(ApplyingTo=job).filter(sender=True).filter(status="Pending")

    return render(request,"code/japplicants.html",{"ppl":ppl,"slug":slug})


def jprofile(request):
    name=request.user
    verifiedJobs=[]
    pendingJobs=[]
    profile=JobProfile.objects.get(username=name)
    verified=JobPortal.objects.filter(name=profile).filter(is_verified=True)
    pending=JobPortal.objects.filter(name=profile).filter(is_verified=False)

    for v in verified:
        verifiedJobs.append(v)

    for p in pending:
        pendingJobs.append(p)

    return render(request,"code\jobProfile.html",{"verifiedJobs":verifiedJobs,"pendingJobs":pendingJobs})





def registerhandlerecruiter(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['username']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1 == pass2:
            userr=CustomUser.objects.create_user(username,email,pass1)
           
            userr.first_name=name
            userr.is_recruiter=True
            userr.save()
            profile=JobProfile(name=name,email=email,username=username)
            profile.save()
            messages.success(request,"you have been registered please login in")
            return redirect("/")
    
    else:
            return HttpResponse("404-something went wrong")



def loginhandlerecruiter(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            txt="you have successfully logged in to the job portal please click on the next button and fill the form to proceed"
            return render(request,"code/sub.html",{'txt':txt})
        else:
            return HttpResponse("something went wrong")


def jobDeclaration(request):
    if request.method=="POST":
 
        name=JobProfile.objects.get(username=request.user)
   
        companyname=request.POST['companyname']
        jr=request.POST['jr']
        jl=request.POST['jl']
        jd=request.POST['jd']
        expectedSalary=request.POST['expectedSalary']
        if expectedSalary:
            JobPortal(name=name,companyname=companyname,jobDescription=jd,expectedSalary=expectedSalary,jTitle=jr,location=jl).save()
        else:
            JobPortal(name=name,companyname=companyname,jobDescription=jd,jTitle=jr,location=jl).save()
        return render(request,"code/waiting.html")

    return render(request,'code/jobDeclaration.html')


def home(request):
    if request.user.is_authenticated:
        n=request.user
        nnn=Profile.objects.filter(username=n).first()

        if len(Intrest.objects.filter(user=nnn))==0:
            return redirect("timeline")      

        


        # i=Intrest.objects.filter(user=n).first().intrest
        # m=Profile.objects.filter(username=n).first().marks
  
        # if i=='' or m==0:
          
        #     return redirect("timeline")
        else:
            return redirect("profile") 
        # else:
        #     return redirect("profile")
    else:
        return render(request,"code/landing.html")

def findppl(request,slug):
    Intrestss=Intrest.objects.all()
    # app=Applicants.objects.filter(ApplyingTo=slug)
    # appl=[]
    # ll=[]
    # for a in app:
    #    appl.append(a.Applicants)
    # for b in Intrestss:
    #     ll.append(b.user)
    
    # diff=set(ll)-set(appl)
    # diff=list(diff)
    # filt=[]
    # for d in diff:
    #     pass

    myFilter=ApplicantFilter(request.GET,queryset=Intrestss)
    Intrestss=myFilter.qs
  

    return render(request,"code/findppl.html",{'myFilter':myFilter,'Intrestss':Intrestss,'slug':slug})

def confirmedjobs(request):
    person=Profile.objects.get(username=request.user)
    App=Applicants.objects.filter(Applicants=person).filter(status="Accepted")
    return render(request,"code/jobconfirmed.html",{'Applicants':App})

def timeline(request):
    n=request.user
    
    # i=Profile.objects.filter(username=n).first().intrest

    # m=Profile.objects.filter(username=n).first().marks
    # if True:
    #     if request.method=="POST":
    #         choice=request.POST['choice']
          
    #         Profile.objects.filter(username=n).update(intrest=choice) 
    if CustomUser.objects.get(username=n).is_recruiter==False:
        test=TestOptions.objects.all()
        if request.method=="POST":
            choice=request.POST['choice']
            a=Profile.objects.filter(username=n).first()
            b=TestOptions.objects.filter(choice=choice).first()
                
            Intrest(user=a,Intrest=b).save()

            return redirect(f"test/{choice}")
        return render(request,"code/choice.html",{"test":test})
    else:
        return redirect("jprofile")
    
    # if m==0:
    #     return redirect("test")
    # return render(request,"base.html")






# def test(request,slug):
    
#     # if Profile.objects.filter(username=n).first().marks == 0:
#     #     choice=Profile.objects.filter(username=n).first().intrest
#     #     if choice=='C++':
#     #         que=Cpp.objects.all()
#     #     if choice=='C':
#     #         que=C.objects.all()
#     #     if choice=='Java':
#     #         que=Java.objects.all()
#     #     if choice=='Python':
#     #         que=Python.objects.all()
        
#         n=request.user
#         choice=TestOptions.objects.filter(choice=slug).first()
#         que=questions.objects.filter(Subject=choice)  
#         question=[]
#         # un=['a','b','c','d','e','f','g','h','i','j']
#         un=['a','b','c','d','e']
        
#         for q in que:
#             if q not in question:
#                 question.append(q)
#             else:
#                 continue
#         sampling = random.sample(question, 5)
#         print("--------------SamPLING111")
#         print(sampling)
#         print("--------------SamPLING111")
#         correctAnswers=[]
#         for j in sampling:
              
#                 correctAnswers.append(j.answer)

#         print("--------------SamPLING222")
#         print(sampling)
#         print("222222222222222222222222222222222222")
#         print(f"{correctAnswers} these are the correct answers")


#         print("--------------SamPLING222")
#         d = dict(zip(un,sampling))
      
#         answers=[]
#         if request.method=="POST":
#             answers.append(request.POST['a'])
#             answers.append(request.POST['b'])
#             answers.append(request.POST['c'])
#             answers.append(request.POST['d'])
#             answers.append(request.POST['e'])
#             # answers.append(request.POST['f'])
#             # answers.append(request.POST['g'])
#             # answers.append(request.POST['h'])
#             # answers.append(request.POST['i'])
#             # answers.append(request.POST['j'])      
    
#             marks=0
#             print(answers)
            
#             for i in range(0,5):
#                 if correctAnswers[i]==answers[i]:
#                     marks=marks+1

#             print(marks)
#             # category=""
#             # if marks == 10:
#             #     category="Legendary"
#             # elif marks>=8 and marks<=9:
#             #     category="Titan"
#             # elif marks>=6 and marks<=7:
#             #     category="Champion"
#             # elif marks>=4 and marks<=5:
#             #     category="Gold"
#             # elif marks>=2 and marks<=3:
#             #     category="Silver"
#             # elif marks>=0 and marks<=1:
#             #     category="Bronze"
            
#             # Profile.objects.filter(username=n).update(marks=marks,category=category)
#             #return redirect("profile")
#         # print("-------------------------------------------------")
#         # print(marks)
#         # print(d)
#         # print("-------------------------------------------------")
#         return render(request,"code/test.html",{'questions':d})







def test(request,slug):
        n=request.user
        choice=TestOptions.objects.filter(choice=slug).first()
        que=questions.objects.filter(Subject=choice)  
        question=[]
     
        un=['a','b','c','d','e','f','g','h','i','j']
        
        for q in que:
            if q not in question:
                question.append(q)
            else:
                continue
        sampling = random.sample(question, 10)
    
        correctAnswers=[]
        for j in sampling:
              
                correctAnswers.append(j.answer)

        waste.objects.all().update(a=correctAnswers[0],b=correctAnswers[1],c=correctAnswers[2],d=correctAnswers[3],e=correctAnswers[4]
        ,f=correctAnswers[5],g=correctAnswers[6],h=correctAnswers[7],i=correctAnswers[8],j=correctAnswers[9],sub=choice)
      
        d = dict(zip(un,sampling))
        return render(request,"code/test.html",{'questions':d})


def cate(marks):
    category=""
    if marks==10:
        category="Legendary"
    elif marks==9:
        category="Titan"
    elif marks==8:
        category="Champion"
    elif marks==7:
        category="Master"
    elif marks==6 or marks==5:
        category="Crystal"
    elif marks==4 or marks==3:
        category="Gold"
    elif marks==2 or marks==1:
        category="Silver"
    else:
        category="Bronze"
    return category



def acceptAnswer(request):
        answers=[]
        if request.method=="POST":
            answers.append(request.POST['a'])
            answers.append(request.POST['b'])
            answers.append(request.POST['c'])
            answers.append(request.POST['d'])
            answers.append(request.POST['e'])
            answers.append(request.POST['f'])
            answers.append(request.POST['g'])
            answers.append(request.POST['h'])
            answers.append(request.POST['i'])
            answers.append(request.POST['j'])

        un=['a','b','c','d','e','f','g','h','i','j']
        x=waste.objects.all().get()
        marks=0
        if x.a==answers[0]:
            marks+=1
        if x.b==answers[1]:
            marks+=1
        if x.c==answers[2]:
            marks+=1
        if x.d==answers[3]:
            marks+=1
        if x.e==answers[4]:
            marks+=1
        if x.f==answers[5]:
            marks+=1
        if x.g==answers[6]:
            marks+=1
        if x.h==answers[7]:
            marks+=1
        if x.i==answers[8]:
            marks+=1
        if x.j==answers[9]:
            marks+=1

        n=Profile.objects.filter(username=request.user).first()
        choice=TestOptions.objects.filter(choice=x.sub).first()
        s=Intrest.objects.order_by('-time').first().time
        #if len(Intrest.objects.filter(user=n).filter(Intrest=choice).filter(marks=marks).filter(time=s))==0:
        if len(Intrest.objects.filter(user=n).filter(Intrest=choice))==0:
            category=cate(marks)
            Intrest(user=n,Intrest=choice,marks=marks,category=category).save()
 
        elif marks>Intrest.objects.filter(user=n).filter(Intrest=choice).get().marks:
            category=cate(marks)
            Intrest.objects.filter(user=n).filter(Intrest=choice).update(category=category,marks=marks,time=datetime.datetime.now())

        else:
            Intrest.objects.filter(user=n).filter(Intrest=choice).update(time=datetime.datetime.now())

        
        txt=f" thanks for giving the test,your score in current test is {marks} you can reappear for this text after 30 days.Right now your best marks will be taken into consideration "
        return render(request,"code/dub.html",{"txt":txt})
        


def dub(request):
    n=request.user 

    return render(request,"code/dub.html",{"s":n})


def loginhandle(request):
    if request.method =="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return HttpResponse("something went wrong")

def logouthandle(request):
    logout(request)
    return redirect("/")

def registerhandle(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']

        if pass1 == pass2:
            userr=CustomUser.objects.create_user(username,email,pass1)
           
            userr.first_name=fname
            userr.last_name=lname
            userr.save()
            profile=Profile(name=fname,email=email,username=username)
            profile.save()
            return redirect("/")
    
    else:
            return HttpResponse("404-something went wrong")

def profile(request):
    username=request.user
    # marks=Profile.objects.filter(username=username).first().marks
    # intrest=Profile.objects.filter(username=username).first().intrest
    # email=Profile.objects.filter(username=username).first().email
    # category=Profile.objects.filter(username=username).first().category
    # n=Profile.objects.filter(username=username).first().name
    # param={
    #     'name':n,
    #     'username':username,
    #     'marks':marks,
    #     'intrest':intrest,
    #     'email':email,
    #     'category':category,
    # }
    user=Profile.objects.filter(username=request.user).get()
   

    tests=Intrest.objects.filter(user=user)

    options = TestOptions.objects.all()


    return render(request,"code/profile.html",{"user":user,"tests":tests,"options":options})

def buddylist(request,slug):
    username=request.user
    user=Profile.objects.filter(username=username).get()
    i=TestOptions.objects.get(choice=slug)
    intrest=Intrest.objects.get(user=user,Intrest=i)
    category=intrest.category

    #all profile
    z=Intrest.objects.filter(category=category).filter(Intrest=i).exclude(user=user)
    z_list=[]
    for s in z:
        z_list.append(s.user)
    
    pending_a=ConnectRequest.objects.filter(sender=user).filter(status="Pending")
    pending_a_list=[]
    pending_b=ConnectRequest.objects.filter(receiver=user).filter(status="Pending")
    pending_b_list=[]
    for p in pending_a:
        pending_a_list.append(p.receiver)
    for p in pending_b:
        pending_b_list.append(p.sender)

    pending=set(pending_a_list).union(set(pending_b_list))
    pending_list=list(pending)


    accepted_a=ConnectRequest.objects.filter(sender=user).filter(status="Accepted")
    accepted_a_list=[]
    accepted_b=ConnectRequest.objects.filter(receiver=user).filter(status="Accepted")
    accepted_b_list=[]
    for p in accepted_a:
        accepted_a_list.append(p.receiver)
    for p in accepted_b:
        accepted_b_list.append(p.sender)

    accepted=set(accepted_a_list).union(set(accepted_b_list))
    accepted_list=list(accepted)


    


    # accepted_a=ConnectRequest.objects.filter(sender=user).filter(status="Accepted")
    # accepted_a_list=[]
    # accepted_b=ConnectRequest.objects.filter(receiver=user).filter(status="Accepted")
    # accepted_b_list=[]
    # for p in accepted_a:
    #     accepted_a_list.append(p.receiver)
    # for p in accepted_b:
    #     accepted_b_list.append(p.receiver)
    # accepted=set(accepted_a_list).union(set(accepted_b_list))
    # print(accepted)
    # accepted_list=[]



    # for p in accepted:
    #     accepted_list.append(p.receiver)
    # print(accepted_list)
    list_to_be_shown=set(z_list)-set(accepted_list)-set(pending_list)
    return render(request,"code/buddylist.html",{'buddy':list_to_be_shown,"pending_list":pending_list,"sub":slug})


#yoo

    # not_to_be_included_list=[]

    # accepted_list=[]
    # list_of_profile=[]
    
    # #pending list
    # not_to_be_included=ConnectRequest.objects.filter(Q(sender__username__icontains=username)).filter(status="Pending")

    # #accepted list
    # liss=ConnectRequest.objects.filter(sender__username__icontains=username).filter(status="Accepted")
    # liss2=ConnectRequest.objects.filter(receiver__username__icontains=username).filter(status="Accepted")

    # for receivers in liss:
    #     accepted_list.append(receivers.receiver)

    # for senders in liss2:
    #     accepted_list.append(senders.sender)


    # #receiver is a foreign key so i am using it for connecting it to the Profile model so that i can iterate the 
    # #informations from the Profile model
    # for receivers in not_to_be_included:
    #     not_to_be_included_list.append(receivers.receiver)
    # all_profile=Profile.objects.filter(category=category).filter(intrest=intrest).exclude(username=username)

    # #typecasting the query set of "all_profile" to a list

    # list_of_profile=list(all_profile)

    # actual_list=set(list_of_profile)-set(not_to_be_included_list)-set(accepted_list)

    # pending_list=not_to_be_included_list
  
    # return render(request,"code/buddylist.html",{'buddy':actual_list,'pendinglist':pending_list})

#done
def budprofile(request,slug):
    bud=Profile.objects.filter(username=slug).first()
    
    return render(request,"code/budprofile.html",{'bud':bud})


#done
def sendrequest(request,receiver,slug):
    receiver_user = Profile.objects.get(username=receiver)
    sender=request.user
    subb=TestOptions.objects.get(choice=slug)
    sender_user=Profile.objects.get(username=sender.username)
    obj,created=ConnectRequest.objects.get_or_create(sender=sender_user,
        receiver=receiver_user,
        status="Pending",
        sub=subb
        
    )
    return redirect("buddylist",slug=slug)

def requestlist(request):
    connectionlist=ConnectRequest.objects.all()
    receiver=request.user.username
    cList=[]
    for connection in connectionlist:
        if connection.receiver.username == receiver and connection.status=="Pending":
            cList.append(connection.sender.username)

    return render(request,"code/pendinglist.html",{'connectionlist':cList})

def declinerequest(request,slug):
    sender=slug
    receiver=request.user.username
    cl=ConnectRequest.objects.all()
    idn=0
    for c in cl:
        if c.receiver.username==receiver and c.sender.username==slug:
            idn=c.idno

    ConnectRequest.objects.filter(idno=idn).delete()
    return redirect("requestlist")


#done
def cancelrequest(request,receiver,slug):
    sender=request.user.username
   
    sen=Profile.objects.get(username=sender)
    rec=Profile.objects.get(username=receiver)
    sub=TestOptions.objects.get(choice=slug)
    # cl=ConnectRequest.objects.all()
    # idn=0
    # for c in cl:
    #     if c.receiver.username==receiver and c.sender.username==sender:
    #         idn=c.idno

    ConnectRequest.objects.filter(sender=sen).filter(receiver=rec).filter(sub=sub).delete()
    return redirect("buddylist",slug=slug)


def acceptrequest(request,slug):
    sender=slug
    receiver=request.user.username
   
    #cl=ConnectRequest.objects.all()
    # idn=0
    # for c in cl:
    #     if c.receiver.username==receiver and c.sender.username==slug:
    #         idn=c.idno
   
    ConnectRequest.objects.filter(Q(sender__username__icontains=sender)).filter(Q(receiver__username__icontains=receiver)).update(status="Accepted")
    

    
    return redirect("requestlist")



def friendlist(request):
    username=request.user.username

    liss=ConnectRequest.objects.filter(sender__username__icontains=username).filter(status="Accepted")
    liss2=ConnectRequest.objects.filter(receiver__username__icontains=username).filter(status="Accepted")

    accepted_list=[]

    for receivers in liss:
        accepted_list.append(receivers.receiver)

    for senders in liss2:
        accepted_list.append(senders.sender)

    return render(request,"code/friendlist.html",{'accepted_list':accepted_list})


def chatting(request,receiver):
    sender=Profile.objects.get(username=request.user)
    rec=Profile.objects.get(username=receiver)
    params1=Message.objects.filter(sender=sender).filter(receiver=rec)
    params2=Message.objects.filter(sender=rec).filter(receiver=sender)
    params= params1 | params2
    p=params.order_by('time')

    return render(request,"code/message.html",{"message":p,"receiver":receiver})


def message(request,receiver):
    print("111")
    if request.method=="POST":
        mess=request.POST['message']
        receiver_user = Profile.objects.get(username=receiver)
        sender=request.user
        sender_user=Profile.objects.get(username=sender.username)

        thread=Message(sender=sender_user,receiver=receiver_user,mess=mess)

        thread.save()

    return redirect("chatting",receiver=receiver)

def retest(request,slug):
    sub=TestOptions.objects.filter(choice=slug).get()
    user=Profile.objects.filter(username=request.user).get()
    if True:
        last_rec=len(Intrest.objects.filter(Intrest=sub).filter(user=user))
        if last_rec!=0:
            s=Intrest.objects.filter(Intrest=sub).filter(user=user).order_by('-time').first().time
            c=datetime.datetime.now()-timedelta(days=30)
 
            if c>s:
                que=questions.objects.filter(Subject=sub)  
                question=[]
        
                un=un=['a','b','c','d','e','f','g','h','i','j']
            
                for q in que:
                    if q not in question:
                        question.append(q)
                    else:
                        continue
                sampling = random.sample(question, 10)
                correctAnswers=[]
                for j in sampling:
                
                    correctAnswers.append(j.answer)

                waste.objects.all().update(a=correctAnswers[0],b=correctAnswers[1],c=correctAnswers[2],d=correctAnswers[3],e=correctAnswers[4]
            ,f=correctAnswers[5],g=correctAnswers[6],h=correctAnswers[7],i=correctAnswers[8],j=correctAnswers[9],sub=sub)
      
                d = dict(zip(un,sampling))
                return render(request,"code/test.html",{'questions':d})
            else:
                 txt="you have recently applied for this test please wait for 30 days and try again"
                 return render(request,"code/dub.html",{"txt":txt})
            

        else:

            return redirect("test",slug=slug)
            
    

        