from django.shortcuts import render, HttpResponse,redirect
from task.forms import TaskForm,TaskModelForm
from task.models import Task
from django.contrib.auth.forms import UserChangeForm


# def home(request):
#     form = TaskForm()
#     if request.method == "POST":
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             # name = form.cleaned_data["name"]
#             # description = form.cleaned_data["description"]
#             # Task.objects.create(name=name, description=description)
#             Task.objects.create(**form.cleaned_data)
#             return HttpResponse("Task is created")
#     context = {'form': form}
#     return render(request, "task/home.html", context)


def home(request):
    form = TaskModelForm()
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponse("Task is created")
    context = {'form': form}
    return render(request, "task/home.html", context)


def list_task(request):
    task_list = Task.objects.all()

    return render(request, 'task/index.html', context={'tasks': task_list})


def task_view(request, task_id):
    task = Task.objects.get(id=task_id)

    return render(request, 'task/task_view.html', {"task_object": task})


def task_delete(request, task_id):
    print(task_id)
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('list_task')


def task_update(request, task_id):
    form = TaskModelForm()
    if request.method == "POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
            Task.objects.filter(id=task_id).update(name=request.POST['name'],
            description=request.POST['description'], status=request.POST['status'])
            return redirect('list_task')
    context = {'form': form}
    return render(request, 'task/task_update.html', context)




