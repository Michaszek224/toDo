from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

def homeView(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        titleOfNewTask = request.POST.get('titleInput')
        newTask = Task.objects.create(title=titleOfNewTask)
        newTask.save()

        return redirect('homeView')

    context = {'tasks': tasks}
    return render(request, 'main/home.html', context)

def completeTask(request, task_id):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        task = Task.objects.get(pk=task_id)
        task.isDone = not task.isDone  # Toggle the isDone field
        task.save()
        return JsonResponse({'message': 'Task status toggled successfully.'})

    return redirect('homeView')
