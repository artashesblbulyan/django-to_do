from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from task.models import Task

class TaskForm(forms.Form):
    name = forms.CharField(max_length=50)
    description = forms.CharField(max_length=1256)


    def clean_name(self):
        _name = self.cleaned_data['name']
        if Task.objects.filter(name=_name).exists():
            raise ValidationError("error")
        return _name




class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"