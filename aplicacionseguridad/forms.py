from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re

# Formulario de Registro
class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

    # Validación personalizada de contraseña
    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        
        # Validar que la contraseña tenga al menos 8 caracteres
        if len(password) < 8:
            raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
        
        # Validar que la contraseña no sea completamente numérica
        if password.isnumeric():
            raise ValidationError('La contraseña no puede ser completamente numérica.')
        
        # Validar que la contraseña no sea demasiado común
        common_passwords = ['123456', 'password', '123456789']
        if password in common_passwords:
            raise ValidationError('La contraseña es demasiado común.')
        
        # Validar que la contraseña no sea similar al nombre de usuario (opcional)
        username = self.cleaned_data.get('username')
        if username.lower() in password.lower():
            raise ValidationError('La contraseña no puede ser similar al nombre de usuario.')
        
        return password# Validación personalizada de contraseña


# Formulario de Login
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
