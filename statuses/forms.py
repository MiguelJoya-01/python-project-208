from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']
        labels = {
            'name': 'Nombre',
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        statuses = Status.objects.filter(name__iexact=name)

        if self.instance.pk:
            statuses = statuses.exclude(pk=self.instance.pk)

        if statuses.exists():
            raise forms.ValidationError(
                'Ya existe un estado con ese nombre.'
            )

        return name
