from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from task.models import Task
from user.forms import UserRegisterForm


class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1256)


    def clean_name(self):
        _name = self.cleaned_data['name']
        if Task.objects.filter(name=_name).exists():
            raise ValidationError("error")
        return _name


def home(request):
    user_form = UserRegisterForm()
    if request.method == "POST":
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():

            user = user_form.save(commit=False)
            user.email = user_form.cleaned_data.get("email")
            user.save()
            return redirect("list_task")
    context = {"form": user_form}

    return render(request, "user/home.html", context)


class TaskUpdateModelForm(forms.ModelForm):
    def clean_name(self):
        _name = self.cleaned_data['name']
        if len(Task.objects.filter(name=_name)) > 1:
            raise ValidationError("error")
        return _name

    class Meta:
        model = Task
        fields = ("name", "description", "status")


class TaskModelForm:
    class Meta:
        model = Task
        fields = "__all__"