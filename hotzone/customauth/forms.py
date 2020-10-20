from django.contrib.auth.forms import AuthenticationForm
from django import forms

class LoginForm(AuthenticationForm):
	username = forms.CharField(
		label='Username', 
		required=True,
		error_messages={
			'required': 'Please enter your username',
		})
	password = forms.CharField(
		widget=forms.PasswordInput(),
		required=True,
		error_messages={
			'required': 'Please enter your password',
		})
	remember_me = forms.BooleanField(required=False)