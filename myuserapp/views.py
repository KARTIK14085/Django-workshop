from django.shortcuts import render
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
                  
