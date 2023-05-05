from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse
import time,datetime,pyqrcode
from django.contrib import messages
from .models import datetime1,contactus, signingup
from django.contrib.auth.models import User,auth
def function1(request):
    return render(request,"index.html")
def function2(request):
    return render(request,"Home.html")
def function3(request):
    return render(request,"about.html")
def function4(request):
    return render(request,"policies.html")
def function5(request):
    return render(request,"claims.html")
def function6(request):
    return render(request,"payment.html")
def function7(request):
    return render(request,"service.html")
def function8(request):
    return render(request,"profile.html")
def function10(request):
    return render(request,"settings.html")
def function11(request):
    return render(request,"help.html")
def function14(request):
    return render(request,"table1.html")
def function15(request):
    return render(request,"ALLSQLcommands.pdf")
def function9(request):
    var1=time.asctime(time.localtime(time.time()))
    data=datetime1(time12=var1)
    data.save()
    return HttpResponse(var1)
def function12(request):
    return render(request, "qrcd.html")
def contactus1(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email = request.POST['email']
        comment = request.POST['comment']
        tosend=comment+'.....................................................This is just an acknowledgement'
        data=contactus(firstname=firstname,lastname=lastname,email=email,comment=comment)
        data.save()
        send_mail(
            'Thank you for contacting HLI System',
            tosend,
            'gvachaspathignaneswar@gmail.com',
            [email],
            fail_silently=False,
        )
        messages.success(request, "Success: This is the sample success Flash message.")
        return render(request, 'service.html')
    else:
        messages.error(request, "Error: This is the sample error Flash message.")
        return render(request,'service.html')
def sign(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        gmail = request.POST['gmail']
        mobile = request.POST['mobile']
        uname = request.POST['uname']
        psswrd = request.POST['psswrd']
        tosend = 'You have successfully Registered'
        sum = signingup(fname=fname, lname=lname, gmail=gmail, mobile=mobile, uname=uname, psswrd=psswrd)
        if signingup.objects.filter(uname=uname).exists():
            messages.info(request, 'Username already exists')
            return render(request,"index.html")
        else:
             sum.save()
             send_mail(
                 'Thank you for contacting HLI System',
                 tosend,
                 'gvachaspathignaneswar@gmail.com',
                 [gmail],
                 fail_silently=False,
             )
             messages.info(request, 'Successfully Registered')
             return render(request, "index.html")
    else:
        messages.info(request, 'Registration Failed')
        return render(request, "index.html")
def checkuserlogin(request):
    un=request.POST["username"]
    pd=request.POST["password"]
    flag=signingup.objects.filter(Q(uname=un) & Q(psswrd=pd))
    print(flag)
    if flag:
        user=signingup.objects.get(uname=un)
        request.session["uname"]=user.uname
        messages.info(request, 'Successfully Logged OUT')
        return render(request,"home.html")
    else:
        messages.info(request, 'Invalid credentials')
        return render(request,"index.html")