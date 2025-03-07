from django.shortcuts import render
from .models import Task
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def get_tasks(request):
    if(request.method == 'POST'):
        serilaizer = TaskSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=201)
        return Response(serilaizer.errors, status=400)
    else:
        tasks = Task.objects.order_by('-created_at').all()
        serilaizer = TaskSerializer(tasks, many=True)
        return Response(serilaizer.data)


# marks as complete
@api_view(['GET','PUT', 'DELETE'])
def handle_task(request, id):
    if(request.method == 'GET'):
        task = Task.objects.get(id=id)
        serilaizer = TaskSerializer(task)
        return Response(serilaizer.data)
    elif(request.method == 'DELETE'):
        task = Task.objects.get(id=id)
        task.delete()
        return Response(status=204)
    else:
        task = Task.objects.get(id=id)
        serilaizer = TaskSerializer(data=request.data)
        if serilaizer.is_valid():
            serilaizer.update(task, request.data)
        return Response(status=200)