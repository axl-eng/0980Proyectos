from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Task
import json

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'generales/task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        
        if title:
            Task.objects.create(user=request.user, title=title, description=description)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'El título es obligatorio'}, status=400)
    else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    task.completed = True
    task.save()
    return JsonResponse({'success': True})

def delete_task(request, task_id):
    try:
        task = Task.objects.get(pk=task_id, user=request.user)
        task.delete()
        return JsonResponse({'success': True})
    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'La tarea no existe'}, status=404)
