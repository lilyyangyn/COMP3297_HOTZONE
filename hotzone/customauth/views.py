from django.views.generic import FormView, View, TemplateView
from .forms import LoginForm, EmailForm, PasswordForm
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib import messages
from urllib import parse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth

class LoginView(FormView):
	template_name = 'auth/login.html'
	form_class = LoginForm
	next_url = ''

	@method_decorator(csrf_protect)
	@method_decorator(never_cache)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		login(self.request, form.get_user())

		remember_me = form.cleaned_data['remember_me']
		if not remember_me:
			self.request.session.set_expiry(0)

		messages.success(self.request, 'Login successfully.')
		return super().form_valid(form)

	def get_success_url(self):
		next_url = self.request.GET.get('next', '')
		if not next_url:
			next_url = reverse('home:homepage')
		return next_url

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			form.add_error('password', 'Please enter the correct username and password.')
			return self.form_invalid(form)

class LogoutView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			logout(request)
			messages.success(request, 'Logout Successfully.')
		return HttpResponseRedirect(reverse('customauth:login'))

class ForgetPwdView(FormView):
	template_name = 'auth/forget_pwd.html'
	form_class = EmailForm
	
	def get_success_url(self):
		return reverse('customauth:email-sent')

class ResetPwdView(FormView):
	template_name = 'auth/reset_pwd.html'
	form_class = PasswordForm
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		old_password = form.cleaned_data['oldpassword']
		username = self.request.user.username
		cur_user = auth.authenticate(username=username, password=old_password)
		if cur_user is not None and cur_user.is_active:
			newpassword = form.cleaned_data['newpassword1']
			cur_user.set_password(newpassword)
			cur_user.save()
			messages.success(self.request, 'Password Update Successfully.')
			return super().form_valid(form)
		else:
			form.add_error('oldpassword', 'Wrong password.')
			return super().form_invalid(form);


	def get_success_url(self):
		return reverse('customauth:login')

class EmailSentView(TemplateView):
	template_name = 'auth/sent_email.html'

class PwdCompleteView(TemplateView):
	template_name = 'auth/complete.html'


