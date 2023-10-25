from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.

def homeView(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        titleOfNewTask = request.POST.get('titleInput')
        newTask = Task.objects.create(title=titleOfNewTask)
        newTask.save()

        return redirect('homeView')


    context = {'tasks':tasks}
    return render(request, 'main/home.html/', context)

