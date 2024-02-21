from typing import Any
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}), label='')
    last_name = forms.CharField(max_length=50, required=True, widget=forms.widgets.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}), label='')
    email = forms.EmailField(required=True, widget=forms.widgets.EmailInput(attrs={'placeholder':'E-mail', 'class':'form-control'}), label='')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args: Any, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'username'
        self.fields['username'].label = ''

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'password'
        self.fields['password1'].label = ''

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''


        
