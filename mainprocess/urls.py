from django.urls import path
from . import views
urlpatterns = [
   
    path('',views.home,name="home"),
    path('timeline',views.timeline,name="timeline"),
    path('test',views.test,name="test"),
    path('profile',views.profile,name="profile"),
    path('loginhandle',views.loginhandle,name="loginhandle"),
    path('registerhandle',views.registerhandle,name="registerhandle"),
    path('logouthandle',views.logouthandle,name="logouthandle"),
    path('buddylist',views.buddylist,name="buddylist"),
    path('requestlist',views.requestlist,name="requestlist"),
    path('bud/<str:slug>',views.budprofile,name="budprofile"),
    path('sendrequest/<str:receiver>',views.sendrequest,name="sendrequest"),
    path('declinerequest/<str:slug>',views.declinerequest,name="declinerequest"),
]
