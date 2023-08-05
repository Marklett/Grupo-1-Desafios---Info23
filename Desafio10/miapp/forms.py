from django import forms
from .models import Users

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')
    
    class Meta:
        model = Users
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de Usuario',
            'email': 'Correo Electrónico',
            'password': 'Contraseña',
        }



class LoginForm(forms.Form):
    username = forms.CharField(label='Nombre de Usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
