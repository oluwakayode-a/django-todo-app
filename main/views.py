from django.shortcuts import render, redirect
from datetime import datetime
from .models import Todo
from .forms import TodoForm
from django.views.decorators.http import require_POST
# Create your views here.

def index(request):
    today = datetime.now()
    todo_list = Todo.objects.order_by('id')
    form = TodoForm()

    context = {'today' : today, 'todo_list' : todo_list, 'form' : form,}
    return render(request, 'main/index.html', context)

@require_POST
def add_todo(request):
    form = TodoForm(request.POST)
    print(request.POST['text'])

    if form.is_valid():
        new_todo = Todo(text=request.POST['text'])
        new_todo.save()

    return redirect('main:index')

def delete_todo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.delete()

    return redirect('main:index')

def delete_all(request):
    todo = Todo.objects.all()
    todo.delete()

    return redirect('main:index')