from django.urls import path
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
    path('',index),
    path('home/',icon),
    path('contactus/',contactus),
    path('shoplogin/',shoplogin),
    path('shopcreate/',shopcreate),
    path('shoprofile/<usr>',shopprofile),
    path('spupload/',spupload),
    path('spedit/<int:id>',spedit),
    path('spviewproduct/',spviewproduct),
    path('itemedit/<int:id>/',itemedit),
    path('itemdelete/<int:id>/',itemdelete),
    path('userlogin/',userlogin),
    path('verify/<auth_token>',verify),
    path('usercreate/',usercreate),
    path('userprofile/',userprofile),
    path('profilebuy/<int:id>',profilebuy),
    path('usreditprofile/<username>',usreditprofile),
    path('usrhelpcenter/',usrhelpcenter),
    path('usraddcart/<int:id>',usraddcart),
    path('cartdisplay/',usrcart),
    path('usrcartremove/<int:id>',usrcartremove),
    path('usrcartbuy/<int:id>',usrcartbuy),
    path('about/',about),
    path("orderplaced/",buyuser)








]
urlpatterns+=staticfiles_urlpatterns()