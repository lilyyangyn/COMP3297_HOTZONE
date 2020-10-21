from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Patient, Virus, Location, Case, Visit
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse

class CustomizedCreateView(CreateView):
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def form_valid(self, form):
		instance = form.save()
		self.kwargs['id'] = instance.pk

		messages.success(self.request, self.success_notice)
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		messages.error(self.request, self.error)
		return super().form_invalid(form)

class CustomizedEditView(UpdateView):
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
	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_object(self, queryset=None):
		return get_object_or_404(self.model, pk=self.kwargs['id'])

	def get(self, *args, **kwargs):
		return self.post(*args, **kwargs)



class PatientAllView(ListView):
	template_name = "record/patient_index.html"
	model = Patient

class PatientShowView(TemplateView):
	template_name = "record/patient_show.html"

	def get_context_data(self, **kwargs):
		patient = get_object_or_404(Patient, pk=self.kwargs['id'])
		context = super().get_context_data()
		context['patient'] = patient
		return context

class PatientCreateView(CustomizedCreateView):
	template_name = "record/patient_new.html"
	model = Patient
	fields = '__all__'
	success_notice = 'Data saved. Creation successfully.'
	error_notice = 'Something is wrong. Creation fails.'

	def get_success_url(self):
		return reverse('records:patient-show', kwargs={'id': self.kwargs['id']})

class PatientEditView(CustomizedEditView):
	template_name = "record/patient_edit.html"
	model = Patient
	fields = '__all__'
	success_notice_changed = 'Data saved. Edit successfully.'
	success_notice_unchanged = 'Data saved. Nothing has changed'
	error_notice = 'Something is wrong. Edition fails.'

	def get_success_url(self):
		return reverse('records:patient-show', kwargs={'id':self.get_object().pk})

class PatientDeleteView(CustomizedDeleteView):
	success_message = 'Delete Successfully.'
	model = Patient

	def get_success_url(self):
		return reverse('records:patients')

