from django.urls import path
from . import views
urlpatterns = [
    path('aboutus',views.aboutus,name="aboutus"),
    path('',views.home,name="home"),
    path('timeline',views.timeline,name="timeline"),
    path('test/<str:slug>',views.test,name="test"),
    path('profile',views.profile,name="profile"),
    path('loginhandle',views.loginhandle,name="loginhandle"),
    path('registerhandle',views.registerhandle,name="registerhandle"),
    path('logouthandle',views.logouthandle,name="logouthandle"),
    path('buddylist/<str:slug>',views.buddylist,name="buddylist"),
    path('friendlist',views.friendlist,name="friendlist"),
    path('requestlist',views.requestlist,name="requestlist"),
    path('bud/<str:slug>',views.budprofile,name="budprofile"),
    path('chat/<str:receiver>',views.chatting,name="chatting"),
    path('chat/message/<str:receiver>',views.message,name="message"),
    path('sendrequest/<str:receiver>/<str:slug>',views.sendrequest,name="sendrequest"),
    path('declinerequest/<str:slug>',views.declinerequest,name="declinerequest"),
    path('acceptrequest/<str:slug>',views.acceptrequest,name="acceptrequest"),
    path('cancelrequest/<str:receiver>/<str:slug>',views.cancelrequest,name="cancelrequest"),
    path('dub',views.dub,name="dub"), 
    path('acceptAnswer',views.acceptAnswer,name="acceptAnswer"),
    path('retest/<str:slug>',views.retest,name="retest"),



    path('jobDeclaration',views.jobDeclaration,name="jobDeclaration"),
    path('loginhandlerecruiter',views.loginhandlerecruiter,name="loginhandlerecruiter"),
    path('registerhandlerecruiter',views.registerhandlerecruiter,name="registerhandlerecruiter"),
    path('jprofile',views.jprofile,name="jprofile"),
    path('findppl/<str:slug>',views.findppl,name="findppl"),
    path('findppl/addapplicant/<str:slug>/<str:name>',views.addapplicant,name="addapplicant"),
    path('seeapplicants/<str:slug>',views.seeapplicants,name="seeapplicants"),
    path('accept/<str:slug>/<str:name>',views.acceptapplicant,name="acceptapplicant"),
    path('reject/<str:slug>/<str:name>',views.declineapplicant,name="declineapplicant"),
    path('confirmedppl/<str:slug>',views.confirmedppl,name="confirmedppl"),


    path('apply',views.apply,name="apply"),
    path('applyto/<str:slug>',views.applyto,name="applyto"),
    path('jrequest',views.jrequest,name="jrequest"),
    path('lresponse',views.lresponse,name="lresponse"),
    path('viewdetailr/<str:slug>',views.viewdetailr,name="viewdetailr"),
    path('viewdetail/<str:slug>',views.viewdetail,name="viewdetail"),
    path('viewdetail2/<str:slug>',views.viewdetail2,name="viewdetail2"),
    path('viewdetailaccept/<str:slug>',views.viewdetailaccept,name="viewdetailaccept"),
    path('viewdetailreject/<str:slug>',views.viewdetailreject,name="viewdetailreject"),
    path('notintrested/<str:slug>',views.notIntrested,name="notIntrested"),


    path('uploaddp',views.uploaddp,name="uploaddp"),
    path('confirmedjobs',views.confirmedjobs,name="confirmedjobs"),



]
