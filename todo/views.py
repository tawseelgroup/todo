from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Task

# Create your views here.

# def home(request):
#     tasks = Task.objects.all()
#     return render(request, 'home.html', {'tasks': tasks})

class TaskView(ListView):
    model = Task
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context
    

def add(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(task=task)
        return redirect('home')
    return render(request, 'home.html')

def update(request):
    if request.method == 'POST':
        ourTask = request.POST
        task_id = ourTask.get('taskupdate')
        # task_id = request.POST.get('taskupdate')
        task = Task.objects.get(id=task_id)
        task.done = True
        task.save()
        return redirect('home')
    return render(request, 'home.html')
