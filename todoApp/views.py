from django.shortcuts import render, redirect

from .forms import TodoForm
from .models import Todo

# Create your views here.
def todo_list(request):
    todos = Todo.objects.filter(complete=False)
    return render(request, 'todoApp/todo_list.html', context={'todos': todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todoApp/todo_detail.html', context={'todo': todo})

def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')

    else:
        form = TodoForm()

    return render(request, 'todoApp/todo_post.html', context={'form': form})

def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')

    else:
        form = TodoForm(instance=todo)

    return render(request, 'todoApp/todo_post.html', context={'form': form})

def done_list(request):
    dones = Todo.objects.filter(complete=True)
    return render(request, 'todoApp/done_list.html', context={'dones': dones})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.complete = True
    todo.save()
    return redirect('todo_list')