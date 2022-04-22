from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponse, redirect
from task.forms import TaskForm, TaskModelForm, TaskUpdateModelForm
from task.models import Task
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm
from user.views import user_login
from django.views.generic import View,ListView,UpdateView,DetailView,DeleteView,CreateView


# class TaskListView(View):
#     def get(self,request):
#         task_list = Task.objects.all()
#         context = {"task_list": task_list}
#         return  render(request, 'task/indexclass.html',context)

class TaskListView(LoginRequiredMixin,ListView):
    model = Task
    ordering = "-created_at"
    template_name = "task_view"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def get_ordering(self):
        order_var = self.request.GET.get('order_by')
        if order_var:
            return order_var
        return super().get_ordering()


# class TaskCreteView(LoginRequiredMixin,View):
#     model = Task
#     template_name = "task/new_task_class.html"
#     success_url = 'task_class_list'
#     form_class = TaskForm
#
#     def get(self, request):
#         form = self.form_class()
#         context = {"task_form": form}
#
#         return render(request, self.template_name,context)
#
#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valide():
#             task = form.save(commit=False)
#             task.user = request.user
#             task.save()
#             messages.succes(request, "create")
#             return redirect(self.success_url)
#         # context = {"task_form": form}
#
#         return render(request, "task/new_tesk_class.html")


class TaskCreteViewGenereic(LoginRequiredMixin,CreateView):
    model = Task
    template_name = "task/new_task_class.html"
    success_url = 'task_class_list'
    form_class = TaskModelForm







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


@login_required(login_url=user_login)
def home(request):
    form = TaskUpdateModelForm()
    if request.method == "POST":
        form = TaskUpdateModelForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            messages.success(request, f"task {form.name} was created successfully")
            return redirect('task_view', task_id=form.id)
        messages.error(request, "error")
    context = {'form': form}
    return render(request, "task/home.html", context)


@login_required(login_url=user_login)
def list_task(request):
    print(request.GET)
    # task_list = Task.objects.filter(user=request.user)
    query_string = request.GET.get('search_task')
    if query_string:
        task_list = request.user.task_set.filter(name__contains=query_string)
    else:
        task_list = request.user.task_set.all()
    return render(request, 'task/index.html', context={'tasks': task_list})


@login_required(login_url=user_login)
def task_view(request, task_id):
    try:
        # task = Task.objects.get(id=task_id, user=request.user)
        task = request.user.task_set.all().get(id=task_id)
    except Task.DoesNotExist:
        return redirect('list_task')
    return render(request, 'task/task_view.html', {"task_object": task})


@login_required(login_url=user_login)
def task_delete(request, task_id):
    try:
        task = request.user.task_set.all().get(id=task_id)
        task.delete()
        messages.success(request, f"task {task.name} was delete  successfully")
    except Task.DoesNoteExist:
        pass
    return redirect('list_task')


@login_required(login_url=user_login)
def task_update(request, task_id):
    # task = Task.objects.get(id=task_id, user=request.user)
    task = request.user.task_set.all().get(id=task_id)
    form = TaskUpdateModelForm(instance=task)
    if request.method == "POST":
        form = TaskModelForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, f"task {task.name} was update successfully")
            return redirect('task_view', task_id=task.id)
    context = {'form': form, "task_object": task}
    return render(request, 'task/task_update.html', context)




