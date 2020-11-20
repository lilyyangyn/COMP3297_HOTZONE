from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapDateInput, BootstrapTextInput, BootstrapUneditableInput

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

class ChangepwdForm(forms.Form):
	oldpassword = forms.CharField(
		required=True,
		label=u"Old password",
		error_messages={'required': u'Please input your old password'},
		widget=forms.PasswordInput(
			attrs={
				'placeholder':u"Old password",
			}
		),
	)
	newpassword1 = forms.CharField(
        required=True,
        label=u"New password",
        error_messages={'required': u'Please input your new password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"New password",
            }
        ),
    )
	newpassword2 = forms.CharField(
        required=True,
        label=u"Confirm password",
        error_messages={'required': u'Please input your new password again'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"Confirm password",
            }
        ),
    )
	
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(u"You need to fill in all blanks")
		elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
			raise forms.ValidationError(u"Two password is not matched.")
		else:
			cleaned_data = super(ChangepwdForm, self).clean()
		return cleaned_data
	
	
