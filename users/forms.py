from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label='Nombre',
        max_length=150,
        required=False,
    )
    last_name = forms.CharField(
        label='Apellidos',
        max_length=150,
        required=False,
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
    first_name = forms.CharField(
        label='Nombre',
        max_length=150,
        required=False,
    )
    last_name = forms.CharField(
        label='Apellidos',
        max_length=150,
        required=False,
    )
    username = forms.CharField(
        label='Nombre de usuario',
        max_length=150,
        required=True,
    )
    password = forms.CharField(
        label='Contraseña',
        required=False,
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password')

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')

        if password:
            user.set_password(password)

        if commit:
            user.save()

        return user
