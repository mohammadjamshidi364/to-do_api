from django.shortcuts import render
import requests


def tasks(request):
    
    url = 'http://localhost:8000/api/tasks'
    
    todo_items = requests.get(url)
    
    
    context = {"todo_items":todo_items.json()}
    
    return render(request , 'todo_app/tasks.html', context)

def task(request , pk):
    
    url = f'http://localhost:8000/api/task/{pk}'
    
    todo = requests.get(url)
    
    
    context = {"todo":todo}
    return render(request , "todo_app/task.html", context)


def createTask(request):
    
    name = request.POST.get('name')
    
    print(name)
    
    url = 'http://localhost:8000/api/create_task/'
    
    
    api_call = requests.post(url , data={'name':name} , json={'Content-type':'application/json'})
    
    
    context = {}
    return render(request , 'todo_app/create_task.html', context)


def deleteTask(request , pk):
    
    url = f'http://localhost:8000/api/delete_task/{pk}/'
    
    api_call = requests.delete(url)
    
    
    context = {}
    return render(request , 'todo_app/delete_task.html' , context)