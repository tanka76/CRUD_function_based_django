from django.shortcuts import render, HttpResponseRedirect
from django.shortcuts import render
from .forms import studentreg 
from .models import user


# Create your views here.
#add new student and show function

def addshow(request):
    if request.method=='POST':
        fm = studentreg(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = user(name=nm,email=em,password=pw)
            reg.save()
            fm = studentreg()

    else:
        fm = studentreg()
    stud = user.objects.all()    
    return render(request,'enroll/addandshow.html',{'form':fm,'std':stud})  

#update student info
def update(request,id):
    if request.method == 'POST':

        pi = user.objects.get(pk=id)
        fm = studentreg(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()     
    else:
        pi = user.objects.get(pk=id)
        fm = studentreg(instance=pi) 
    return render(request,'enroll/update.html',{'form':fm})
    
    
# delete student
def deletestd(request, id):
    dm = user.objects.get(pk=id)
    dm.delete()
    return HttpResponseRedirect('/')


