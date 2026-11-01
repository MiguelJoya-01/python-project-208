from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nombre',
        max_length=150,
        required=True,
    )
    last_name = forms.CharField(
        label='Apellidos',
        max_length=150,
        required=True,
    )
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=150,
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Contraseña (confirmación)'


    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'username')


class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
