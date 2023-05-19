from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializers import TaskSerializer
from .models import Task

@api_view(['GET'])
def tasks(request):
    todo_items = Task.objects.all().order_by('-updated')
    serializer = TaskSerializer(todo_items , many=True)
    
    return Response(serializer.data)

@api_view(['GET'])
def task(request , pk):
    todo = Task.objects.get(id=pk)
    serializer = TaskSerializer(todo)
    
    return Response(serializer.data)

@api_view(['POST'])
def createTask(request):
    
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
    return Response({"item was added "})

@api_view(['POST'])
def updateTask(request , pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task , data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("item was updated")

@api_view(['DELETE'])
def deleteTask(request , pk):
    todo = Task.objects.get(id=pk)
    todo.delete()
    return Response({"message":"item was deleted"})
