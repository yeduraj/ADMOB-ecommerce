import os
import uuid

from django.contrib import messages
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from ecomproject.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from .forms import *
from .models import *


# Create your views here.

def index(request):
    return render(request,'index.html')
def icon(request):
    return render(request,"index.html")

def contactus(request):
    return render(request,'contactus.html')
def shopcreate(request):
    if request.method=="POST":
        a=spcreateform(request.POST)
        if a.is_valid():
            sname=a.cleaned_data['shopname']
            usr=a.cleaned_data['username']
            ps=a.cleaned_data['password']
            cps=a.cleaned_data['cpassword']
            em=a.cleaned_data['email']
            ph=a.cleaned_data['phone']
            if cps==ps:
                b=spcreatemodel(shopname=sname,username=usr,password=ps,email=em,phone=ph)
                b.save()
                return redirect(shoplogin)
            else:
                return HttpResponse('failed')
    return render(request,'shopcreate.html')

def shoplogin(request):
    if request.method=="POST":
        a=sploginform(request.POST)
        if a.is_valid():
            usr=a.cleaned_data['username']
            ps=a.cleaned_data['password']
            b=spcreatemodel.objects.all()
            for i in b:

                if usr==i.username and ps==i.password:
                    id1=i.id
                    request.session['id']=id1

                    return redirect(f'/shoprofile/{usr}') # shoprofile is url
            else:
                return HttpResponse('failed')

    return render(request,'shoplogin.html')

def shopprofile(request,usr):
    id=request.session['id']
    return render(request,'shopprofie.html',{'usr':usr,'id':id})

#  threefunction used for shop upload shop edit shop view product
def spupload(request):
    if request.method=="POST":
        a=spuploadform(request.POST,request.FILES)
        if a.is_valid():

            pname=a.cleaned_data['ptname']
            pid=a.cleaned_data['ptid']
            ptimg=a.cleaned_data['ptimage']
            ptpr=a.cleaned_data['ptprice']
            dsc=a.cleaned_data['desc']
            b=spuploadmodel(ptname=pname,ptid=pid,ptimage=ptimg,ptprice=ptpr,desc=dsc)
            b.save()
            return redirect(spviewproduct)
        else:
            return HttpResponse('upload failed...')
    return render(request,'shupload.html')


def spedit(request,id):
    a=spcreatemodel.objects.get(id=id)
    if request.method=="POST":
        a.shopname=request.POST.get('shopname')
        a.username=request.POST.get('username')
        a.password=request.POST.get('password')
        a.email=request.POST.get('email')
        a.phone=request.POST.get('phone')
        a.save()
        return HttpResponse('edit successfull')

    return render(request,'shedit.html',{'a':a})


def spviewproduct(request):
    x = spuploadmodel.objects.all()
    pnm = []
    pid = []
    pimg = []
    ppri = []
    dsc = []
    id=[]
    for i in x:
        pnm.append(i.ptname)
        pid.append(i.ptid)
        pimg.append(str(i.ptimage).split('/')[-1])
        ppri.append(i.ptprice)
        dsc.append(i.desc)
        w=i.id
        id.append(w)
    mylist = zip(pimg,pid,pnm,ppri,dsc,id)
    return render(request,'shviewproduct.html',{'mylist':mylist})

# used for edit the item
def itemedit(request,id):
    a=spuploadmodel.objects.get(id=id)
    im=str(a.ptimage).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES)>0:
            if len(a.ptimage)>0:
                os.remove(a.ptimage.path)
            a.ptimage=request.FILES['ptimage']
        a.ptname=request.POST.get('ptname')
        a.ptid=request.POST.get("ptid")
        a.ptprice=request.POST.get('ptprice')
        a.desc=request.POST.get('desc')
        a.save()
        return redirect(spviewproduct)
    return render(request,'spitemedit.html',{'a':a,'im':im})

# used for delete the item.
def itemdelete(request,id):
    a=spuploadmodel.objects.get(id=id)
    if len(a.ptimage)>0:
        os.remove(a.ptimage.path)
    a.delete()
    return redirect(spviewproduct)




def usercreate(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if User.objects.filter(username=username).first():
            messages.success(request, 'username already taken')
            return redirect(usercreate)
        if User.objects.filter(email=email).first():
            messages.success(request, 'email already taken')
            return redirect(usercreate)
        user_obj=User(username=username,email=email,first_name=first_name,last_name=last_name)
        if password==cpassword:
            user_obj.set_password(password)
            user_obj.save()
        auth_token = str(uuid.uuid4())
        profile_obj = profile.objects.create(user=user_obj, auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email, auth_token)
        return HttpResponse("success")
    return render(request,'usercreate.html')

def send_mail_regis(email,auth_token):
    subject="your account has been verified"
    message=f'paste the link to verify your account http://127.0.0.1:8000/verify/{auth_token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    send_mail(subject,message,email_from,recipient)

def verify(request,auth_token):
    profile_obj=profile.objects.filter(auth_token=auth_token).first()
    if profile_obj:
        if profile_obj.is_verified:
            messages.success(request,'your account is already verified')
            return redirect(userlogin)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,'your account has been verified')
        return redirect(userlogin)
    else:
        messages.success(request,"user not found")
        return redirect(userlogin)



def userlogin(request):
    if request.method=="POST":
        username = request.POST.get('username')
        request.session['username']=username
        print(request.session['username'])
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()



        if user_obj is None:
            messages.success(request, 'user not found')
            return redirect(userlogin)
        profile_obj = profile.objects.filter(user=user_obj).first()
        if not profile_obj.is_verified:
            messages.success(request, 'profile not verified check your email')
            return redirect(userlogin)
        user = authenticate(username=username, password=password)
        if user is None:
            messages.success(request, 'wrong password or username')
            return redirect(userlogin)

        return redirect(userprofile)
    return render(request,'userlogin.html')


# edit this function
def profilebuy(request,id):
    username=request.session['username']
    a=spuploadmodel.objects.get(id=id)
    if request.method == 'POST':
        ptname = request.POST.get('ptname')
        ptprice = request.POST.get('ptprice')
        item_quantity = request.POST.get('quantity')
        total = int(ptprice) * int(item_quantity)
        return render(request, 'finalbill.html', {'a': ptname, 'b': item_quantity, 'c': total, 'd': ptprice})

    pr = a.ptprice
    nm = a.ptname
    ii = a.id
    return render(request,'usercartbuy.html',{'a':a,'x':pr,'y':nm,'z':ii,'username':username})



def userprofile(request):
    x = spuploadmodel.objects.all()

    pnm = []
    id = []
    pimg = []
    ppri = []
    dsc = []

    for i in x:
        pnm.append(i.ptname)
        pimg.append(str(i.ptimage).split('/')[-1])
        ppri.append(i.ptprice)
        dsc.append(i.desc)
        w = i.id
        id.append(w)
    mylist = zip(pimg,id, pnm, ppri, dsc)
    u=request.session['username']
    return render(request, 'userprofile.html', {'mylist': mylist,'u':u})


def usraddcart(request,id):
    a=spuploadmodel.objects.get(id=id)
    if a:
       b=cart(ptname=a.ptname,ptid=a.ptid,ptimage=a.ptimage,ptprice=a.ptprice,desc=a.desc)
       b.save()
       return render(request,'addtocart.html')


    return render(request,'useraddcart.html')



def usreditprofile(request,username):
    a=User.objects.get(username=username)
    if request.method=="POST":
        a.username=request.POST.get('username')
        a.email=request.POST.get('email')
        a.first_name=request.POST.get('first_name')
        a.last_name=request.POST.get('last_name')
        a.save()
        return HttpResponse('success')


    return render(request,'usereditprofile.html',{'a':a})

def usrcart(request):
    a=cart.objects.all()
    pnm = []
    id = []
    pimg = []
    ppri = []
    dsc = []

    for i in a:
        pnm.append(i.ptname)
        pimg.append(str(i.ptimage).split('/')[-1])
        ppri.append(i.ptprice)
        dsc.append(i.desc)
        w = i.id
        id.append(w)
    mylist = zip(pimg, id, pnm, ppri, dsc)

    return render(request,'usercart.html',{'mylist':mylist})

def usrcartremove(request,id):
    a=cart.objects.get(id=id)
    a.delete()
    return redirect(usrcart)


def usrcartbuy(request,id):
    a=cart.objects.get(id=id)
    im=str(a.ptimage).split('/')[-1]
    if request.method == 'POST':
        ptname = request.POST.get('ptname')
        ptprice = request.POST.get('ptprice')
        item_quantity = request.POST.get('quantity')
        total = int(ptprice) * int(item_quantity)
        return render(request, 'finalbill.html', {'a': ptname, 'b': item_quantity, 'c': total, 'd': ptprice})
    pr = a.ptprice
    nm = a.ptname
    ii = a.id
    return render(request,'usercartbuy.html',{'a':a,'im':im,'x':pr,'y':nm,'z':ii,})


def usrhelpcenter(request):

    return render(request,'userhelpcenter.html')

def about(request):
    return render(request,"about.html")

def buyuser(request):
    return render(request,"orderplaced.html")