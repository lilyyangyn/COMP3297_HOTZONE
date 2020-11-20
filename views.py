import django
from django import template
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required
from django.template.base import kwarg_re
from django.urls.base import is_valid_path, reverse

from .forms import LoginForm, EmailForm, ChangepwdForm
from django.views.generic import TemplateView, View, FormView

from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect



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
			messages.error(request, 'Please enter the correct username and password')
			return self.form_invalid(form)

class LogoutView(FormView):
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

@login_required
def ResetPwdView(request):
	if request.method == 'POST':
		form = ChangepwdForm(request.POST)
		if form.is_valid():
			username = request.user.username
			oldpassword = form.cleaned_data['oldpassword']
			user = auth.authenticate(username=username, password=oldpassword)
			if user is not None and user.is_active:
				newpassword = form.cleaned_data['newpassword1']
				user.set_password(newpassword)
				user.save()
				return HttpResponseRedirect('login')
			else:
				return render(request,'auth/reset_pwd.html',{'form':form,'message':'Wrong password.'})
	else:
		form=ChangepwdForm()
	return render(request,'auth/reset_pwd.html',{'form':form})


class EmailSentView(TemplateView):
	template_name = 'auth/sent_email.html'

class PwdCompleteView(TemplateView):
	template_name = 'auth/complete.html'