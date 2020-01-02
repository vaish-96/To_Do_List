from django.shortcuts import render,redirect
from testapp.models import Add
# Create your views here.

def home(request):
    if request.method == "POST":
        adds = Add(title = request.POST['titles'])
        adds.save()
        return redirect('/')
    else:
        add = Add.objects.all()    
        return render(request,'home.html',{'add':add})

def delete(request,id):
    add = Add.objects.get(id=id)
    add.delete() 
    return redirect('home')

