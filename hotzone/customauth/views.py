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
		return HttpResponseRedirect(self.get_success_url())

	def get_success_url(self):
		redirect_url = self.success_url if self.success_url else self.next_url

		nextLocation = parse.urlparse(redirect_url)
		isSameHost = (nextLocation == self.request.get_host())

		if not (redirect_url and isSameHost):
			redirect_url = reverse('records:patients')
		return redirect_url

	def get(self, request, *args, **kwargs):
		self.next_url = request.GET.get('next', '')
		return super(LoginView, self).get(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		form_class = self.get_form_class()
		form = self.get_form(form_class)
		if form.is_valid():
			return self.form_valid(form)
		else:
			messages.error(request, 'Login fails.')
			return self.form_invalid(form)

class LogoutView(View):
	def get(self, request, *args, **kwargs):
		if request.user.is_authenticated:
			logout(request)
			messages.success(request, 'Logout Successfully.')
		return HttpResponseRedirect(reverse('customauth:login'))






