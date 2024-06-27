from django import forms
from .models import Task

class CreateTaskForm(forms.ModelForm):
    due_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],
    )
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date', 'category', 'assigned_to']
