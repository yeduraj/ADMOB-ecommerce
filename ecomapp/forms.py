from django import forms   # need to import forms
# forms-->modules-->Form(inherit)
# shop create
class spcreateform(forms.Form):
    shopname=forms.CharField(max_length=30)
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)
    email=forms.EmailField()
    phone=forms.IntegerField()
# shop login
class sploginform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)

class spuploadform(forms.Form):
    ptname=forms.CharField(max_length=30)
    ptid=forms.IntegerField()
    ptimage=forms.FileField()
    ptprice=forms.IntegerField()
    desc=forms.CharField(max_length=60)

class usrcreateform(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=35)
    last_name = forms.CharField(max_length=35)
    password = forms.CharField(max_length=25)
    cpassword = forms.CharField(max_length=25)
