from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_password(self):
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')

        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('Проверьте пароли')
        return pass2
    

class LoginForm(forms.Form):
    email = forms.EmailField(label='Почта', required=True, max_length=254)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email = email, password=password)
        if not user:
            raise forms.ValidationError('неверные почта или пароль')
        return self.cleaned_data
    