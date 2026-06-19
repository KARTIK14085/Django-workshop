from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from .models import student

# Create your views here.
def mailsenddemo(request):
    subject = 'Welcome '
    message = ' thank you for choosing us'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['kartik123489@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Mail Sent")

def homepage(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def shop(request):
    return render(request,'shop.html')
def contactprocess(request):
    a = int(request.POST['txt1'])
    b = int(request.POST['txt2'])
    e = int(request.POST['txt3'])
    c = a + b + e
    d=""
    if c >= 90:
        d = "A+"
    elif  c>= 80:
        d = "A"
    elif  c >= 70:
        d = "B"
    elif  c >= 60:
        d = "C"
    elif  c >= 50:
        d = "D"
    else:
        d = "F"

    return render(request,'ans.html',{'mya':a,'myb':b,'myc':c,'myd':d})

def savesessiondata(request):
    msg=request.session['username']="LUCIFER"
    return HttpResponse("session created",msg)

def savesessiondata2(request):
    msg=request.session['username']="LUCIFER"
    return HttpResponse("session created 2",msg)

def getsessiondata(request):
    msg=request.session.has_key('username')
    return HttpResponse("get created",msg)

def delsessiondata(request):
    msg=request.session['username']
    return HttpResponse("session delete",msg)

def login(request):
    return render(request,'login.html')

def loginprocess(request):
    txt1= request.POST['username']
    request.session['username']="LUCIFER"
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('username'):
        return render(request,"dashboard.html")
    else:
        return redirect(login)

def logout(request):
    del request.session['username']
    return redirect(login)

def emailform(request):
    Name = request.POST.get("name")
    Email = request.POST.get("email")
    Contact = request.POST.get("contact")

    mymsg = " Hello has Contact you",Name," Email is ",Email," Contact is ",Contact

    subject = 'Contact us from website'
    email_from = settings.EMAIL_HOST_USER

    message = mymsg
    recipient_list = ['k@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Thank you for Contacting us.")

def studentform(request):
    return render(request,'studentform.html')

def studentformprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    student.objects.create(sname=txt1,email=txt2,mobile=txt3,address=txt4)
    return HttpResponse("Thank you for Contacting us.")
   # mymsg1 = f"Hello, {txt1} has contacted you. Email is {txt2}. Contact is {txt3}. Address is {txt4}"

    #subject = 'Contact us from website'
    #email_from = settings.EMAIL_HOST_USER

   # message = mymsg1
  #  recipient_list = ['k@gmail.com',]
  #  send_mail( subject, message, email_from, recipient_list )
def displaystudent(request):
    mystudentlist = student.objects.all()
    return render(request,'displaystudent.html',{'mydata':mystudentlist})

def deletestudent(request,id):
    student.objects.get(id=id).delete()
    return redirect(displaystudent)


    
    
                  
