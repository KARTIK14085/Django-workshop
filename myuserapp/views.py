from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
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


                  
