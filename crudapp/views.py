from django.shortcuts import render,redirect

# Create your views here.
from .forms import crudForm
from .models import crud


def create(request):
    if request.method =="POST":
        a = crudForm(request.POST,request.FILES)
        if a.is_valid():
            a.save()
        else:pass
    else:
        a=crudForm()    
    data = crud.objects.all()    
    return render(request,'create.html' , {'fm':a,'data':data})


def update(request ,id):
    b=crud.objects.get(id= id)
    data = crud.objects.all()
    c=crudForm(instance=b)
    if request.method=="POST":
        a=crudForm(request.POST,request.FILES,instance=b )
        if a.is_valid():
            a.save()
            return redirect('create')
            
    else:
        return render(request,'create.html',{'fm':c,'data':data})    
    return render(request,'create.html',{'fm':c,'data':data})    



def delete(request , id):
    d = crud.objects.filter(id=id).delete()
    return redirect('create')