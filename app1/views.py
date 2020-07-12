from django.shortcuts import render,redirect
from app1.models import NesclassModel
from django.contrib import messages
# Create your views here.
def adminLoginl(request):
    return render(request,'adminlogin.html')


def adminlog(request):
    name=request.POST.get('t1')
    pwd=request.POST.get('t2')

    if name =='admin' and pwd =='admin':
        return render(request,'menu.html')
    else:

        return render(request,'adminlogin.html',{'error':'login fail'})


def newclass(request):
    return render(request,'newclass.html')


def savedb(request):
    n=request.POST.get('t1')
    fa=request.POST.get('t2')
    da=request.POST.get('t3')
    t=request.POST.get('t4')
    f=request.POST.get('t5')
    d=request.POST.get('t6')
    print(n,fa,da,t,f,d,)
    try:
        NesclassModel(name=n,faculty=fa,date=da,time=t,fee=f,duration=d).save()
        return render(request,'newclass.html',{'msg':'saved success'})
    except NesclassModel.DoesNotExist:

        return render(request,'newclass.html',{'msg':'not saved'})


def viewall(request):
    data=NesclassModel.objects.all()
    return render(request,'viewall.html',{'data':data})


def update(request):
    num=request.GET.get('no')
    #print(num)
    data=NesclassModel.objects.get(id=num)
    #print(data)
    return render(request,'update.html',{'data':data})


def updatedata(request):
    no=request.GET.get('no')
    n=request.POST.get('t1')
    fa=request.POST.get('t2')
    da=request.POST.get('t3')
    ti=request.POST.get('t4')
    f=request.POST.get('t5')
    d=request.POST.get('t6')
    print(no,n,fa,da,ti,f,d,)
    if ti and da:
        NesclassModel.objects.filter(id=no).update(name=n,faculty=fa,date=da,time=ti,fee=f,duration=d)
        messages.success(request,'updated success')
        return viewall(request)
        #return render(request,'viewall.html')
    else:
        messages.error(request,'not update')
        return viewall(request)


def delete(request):
    d=request.GET.get('del')
    print(d)
    NesclassModel.objects.filter(id=d).delete()
    messages.success(request,'Deleted successful')
    return redirect('viewall')


def some(request):
    return render(request,'menu.html')