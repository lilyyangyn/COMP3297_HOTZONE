from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages

class CustomizedListView(ListView):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_queryset(self):
		object_list = self.model.objects.filter(**self.get_filters())
		return object_list

class CustomizedShowView(TemplateView):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_context_data(self, **kwargs):
		instance = get_object_or_404(self.model, pk=self.kwargs['id'])
		context = super().get_context_data()
		context[self.instanceName] = instance
		return context

class CustomizedCreateView(CreateView):
	success_notice = 'Data saved. Creation successfully.'
	error_notice = 'Something is wrong. Creation fails.'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		instance = form.save()
		self.kwargs['id'] = instance.pk

		messages.success(self.request, self.success_notice)
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		messages.error(self.request, self.error_notice)
		return super().form_invalid(form)

class CustomizedEditView(UpdateView):
	success_notice_changed = 'Data saved. Edit successfully.'
	success_notice_unchanged = 'Data saved. Nothing has changed'
	error_notice = 'Something is wrong. Edition fails.'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_object(self, queryset=None):
		return get_object_or_404(self.model, pk=self.kwargs['id'])

	def form_valid(self, form):
		if form.has_changed():
			instance = form.save()
			messages.success(self.request, self.success_notice_changed)
		else:
			messages.info(self.request, self.success_notice_unchanged)

		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		messages.error(self.request, self.error_notice)
		return super().form_invalid(form)

class CustomizedDeleteView(DeleteView):
	success_message = 'Delete Successfully.'
	
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_object(self, queryset=None):
		return get_object_or_404(self.model, pk=self.kwargs['id'])

	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)

	def delete(self, request, *args, **kwargs):
		messages.success(self.request, self.success_message)
		return super().delete(request, *args, **kwargs)