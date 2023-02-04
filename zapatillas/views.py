from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
from zapatillas import views
from .forms import TaskForm
from django.template import Template, Context, loader
from zapatillas.models import Project, Zapatillas, Entrega, Task

def plantilla1 (request):
    return render(request, 'plantilla1.html')

def listado (request):
    tasks = Task.objects.all()
    return render (request, 'listado.html', {'tasks': tasks})

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'formularionuevo.html', {
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password1']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login (request, user)
                return redirect('task')
            except IntegrityError:
                return render(request, 'formularionuevo.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario existente'
                })
        return render(request, 'formularionuevo.html', {
            'form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
        })    

@login_required
def create_task(request):

    if request.method == 'GET':
        return render(request, 'createtask.html', {
            'form': TaskForm
    })
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task')
        except ValueError:
            return render(request, 'createtask.html', {
                'form': TaskForm,
                'error': 'Por favor escriba datos validos'
            })

@login_required
def task_detalle(request, task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render (request, 'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('task')
        except ValueError:
            return render (request, 'task_detail.html', {'task': task, 'form': form,
            'error': "Error en la actualización"})

@login_required
def task_eliminar(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('task')

@login_required
def create_zapatilla(request):
    return render(request, 'createzapatilla.html', {
        'form': TaskForm
    })

def signout(request):
    logout(request)
    return redirect('task')

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecto.'
            })
        else:
            login(request, user)
            return redirect('task')

def about (request):
    return render (request, 'about.html')



    
