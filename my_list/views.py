from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home_view(request):
    tasks = Task.objects.all()  # Get all tasks
    return render(request, 'home.html', {'tasks': tasks})
def add_view(request):
    if request.method == "POST":
        taskname = request.POST.get('taskname')
        description = request.POST.get('description')
        date = request.POST.get('date')
        priority = request.POST.get('priority')
        status = request.POST.get('status') == 'on'  # Check if the checkbox is checked

        new_task = Task(
            taskname=taskname,
            description=description,
            date=date,
            priority=priority,
            status=status
        )
        new_task.save()  # Save the task to the database
        return redirect('home')  # Redirect to home after adding

    return render(request, 'add_task.html')

def update_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)  # Get the task or return 404
    if request.method == "POST":
        task.taskname = request.POST.get('taskname')
        task.description = request.POST.get('description')
        task.date = request.POST.get('date')
        task.priority = request.POST.get('priority')
        task.status = request.POST.get('status') == 'on'  # Checkbox for completion status
        task.save()  # Save changes
        return redirect('home')  # Redirect to home after editing

    return render(request, 'update_task.html', {'task': task})



def delete_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def task_detail_view(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})