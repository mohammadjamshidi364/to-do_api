from django.shortcuts import render , redirect
import requests


def tasks(request):
    
    url = 'http://localhost:8000/api/tasks'
    
    todo_items = requests.get(url)
    
    
    context = {"todo_items":todo_items.json()}
    
    return render(request , 'todo_app/tasks.html', context)

def task(request , pk):
    
    url = f'http://localhost:8000/api/task/{pk}'
    
    todo = requests.get(url)
    
    
    context = {"todo":todo.json()}
    return render(request , "todo_app/task.html", context)


def createTask(request):
    if request.method == "POST":
        name = request.POST.get('name')
        
        
        url = 'http://localhost:8000/api/create_task/'
        
        
        api_call = requests.post(url , data={'name':name} , json={'Content-type':'application/json'})
        return redirect('home')
    
    
    context = {}
    return render(request , 'todo_app/create_task.html', context)


def updateTask(request , pk):
    url = f'http://localhost:8000/api/task/{pk}'
    
    todo = requests.get(url)
    if request.method == "POST":
        
        name = request.POST.get('name')
        complete = request.POST.get('completed')
        if complete == "completed":
            completed = True
        else:
            completed = False
        
        url = f'http://localhost:8000/api/update_task/{pk}/'
        
        api_call = requests.post(url ,data={'name':name , "completed":completed } , json={'Content-type':'application/json'})
        return redirect('home')
    
    context = {'todo':todo.json()}
    return render(request, 'todo_app/update_task.html', context)

def deleteTask(request , pk):
    
    if request.method == "POST":    
        url = f'http://localhost:8000/api/delete_task/{pk}/'
        
        api_call = requests.delete(url)
        return redirect('home')
    
    context = {}
    return render(request , 'todo_app/delete_task.html' , context)