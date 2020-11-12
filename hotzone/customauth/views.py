from django.views.generic import FormView, View
from .forms import LoginForm
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.contrib import messages
from urllib import parse
from django.urls import reverse

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

class LogoutView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			logout(request)
			messages.success(request, 'Logout Successfully.')
		return HttpResponseRedirect(reverse('customauth:login'))






