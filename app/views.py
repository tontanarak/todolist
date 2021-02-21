from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def index(request):
    tasks = Tasks.objects.reverse().all()
    return render(request,'index.html',{'task':tasks})

def add(request):
    tasks = Tasks.objects.all()
    name =  request.POST['name']
    tasks.create(
        name=name
    )
    return redirect('/')

def edit(request,pk):
    tasks = Tasks.objects.filter(id=pk)
    med =  request.POST['method']
    name = request.POST['name']
    if med == 'edit':
        tasks.update(name=name)
        
    elif med == '-':
        tasks.delete()
    
    elif med == '✓':
        tasks.update(comp=True)
    return redirect('/')