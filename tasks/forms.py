from django import forms

from .models import Label


class LabelForm(forms.ModelForm):
    class Meta:
        model = Label
        fields = ['name']
        labels = {
            'name': 'Nombre',
        }

    def clean_name(self):
        name = self.cleaned_data['name']

        labels = Label.objects.filter(name__iexact=name)

        if self.instance.pk:
            labels = labels.exclude(pk=self.instance.pk)

        if labels.exists():
            raise forms.ValidationError(
                'Ya existe una etiqueta con ese nombre.'
            )

        return name
