from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'labels',
        ]
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'status': 'Estado',
            'executor': 'Ejecutor',
            'labels': 'Etiquetas',
        }

