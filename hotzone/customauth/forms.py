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
	oldpassword = forms.CharField(
		widget=forms.PasswordInput(),
		required=True,
		label=u"Old password",
		error_messages={'required': u'Please input your old password'},
	)
	newpassword1 = forms.CharField(
        required=True,
        label=u"New password",
        error_messages={'required': u'Please input your new password'},
        widget=forms.PasswordInput(),
    )
	newpassword2 = forms.CharField(
        required=True,
        label=u"Confirm password",
        error_messages={'required': u'Please input your new password again'},
        widget=forms.PasswordInput(),
    )

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get("newpassword1")
		confirm_password = cleaned_data.get("newpassword2")

		if password != confirm_password:
			self.add_error('newpassword2', "Two passwords not match.")
			raise forms.ValidationError("Two passwords not match.")

		return cleaned_data
