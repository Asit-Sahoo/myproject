from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
#from .forms import usersForm
def homePage(request):
    return render(request,"index.html")
def submitform(request):
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                #'form':fn,
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            
            return HttpResponse(finalans)
    except:
        pass
def services(request):
    return render(request,"services.html")
def client(request):
    return render(request,"client.html")
def contact(request):
    if request.method=='GET':
        output=request.GET.get('output')
    return render(request,"contact.html",{'output':output})
def cal(request):
    finalans=0
    #fn=usersForm()
    data={}
    try:
        if request.method=="POST":
            n1=int(request.POST.get('num1'))
            n2=int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                #'form':fn,
                'n1':n1,
                'n2':n2,
                'output':finalans
            }
            url="/contact/?output={}".format(finalans)
            return HttpResponseRedirect(url)
    except:
        pass
    return render(request,"cal.html",data)
def coursedetails(request,courseid):
    return HttpResponse(courseid)
    
