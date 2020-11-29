from django.views.generic import TemplateView
from .forms import ClusterCreateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse

class ClusterNewView(TemplateView):
	template_name = 'clustering/new.html'
	form_class = ClusterCreateForm

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		# TODO: Clustering
		messages.success(self.request, 'Succeed.')

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form = ClusterCreateForm(self.request.GET or None)
		context['form'] = form

		return self.render_to_response(context)