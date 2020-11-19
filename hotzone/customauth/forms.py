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

class EmailForm(forms.Form):
	email_addr = forms.EmailField(required=True)
	def send_email(self,form):
		pass

class PasswordForm(forms.Form):
	new_password = forms.CharField(
		widget=forms.PasswordInput(),
		required=True,
		error_messages={
			'required': 'Please enter your password',
		})
	new_password_confirm = forms.CharField(
		widget=forms.PasswordInput(),
		required=True,
		error_messages={
			'required': 'Please enter your password',
		})

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get("new_password")
		confirm_password = cleaned_data.get("new_password_confirm")

		if password != confirm_password:
			raise forms.ValidationError(
				"Password and confirm_password does not match"
				)
