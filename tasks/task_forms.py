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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['executor'].label_from_instance = (
            lambda user: user.get_full_name() or user.username
        )

    def clean_name(self):
        name = self.cleaned_data['name']

        tasks = Task.objects.filter(name__iexact=name)

        if self.instance.pk:
            tasks = tasks.exclude(pk=self.instance.pk)

        if tasks.exists():
            raise forms.ValidationError(
                'Ya existe una tarea con ese nombre.'
            )

        return name
