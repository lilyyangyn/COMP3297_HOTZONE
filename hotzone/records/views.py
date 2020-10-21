from django.views.generic import ListView, TemplateView
from django.views.generic.edit import UpdateView
from .models import Patient, Virus, Location, Case, Visit
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse

class PatientAllView(ListView):
	template_name = "record/patient_index.html"
	model = Patient

class PatientDetailView(TemplateView):
	template_name = "record/patient_detail.html"

	def get_context_data(self, **kwargs):
		patient = Patient.objects.get(pk=self.kwargs['id'])
		context = super().get_context_data()
		context['patient'] = patient
		return context

class PatientEditView(UpdateView):
	template_name = "record/patient_edit.html"
	model = Patient
	fields = '__all__'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_object(self, queryset=None):
		return get_object_or_404(self.model, pk=self.kwargs['id'])

	def form_valid(self, form):
		if form.has_changed():
			form.save()
			messages.success(self.request, 'Data saved. Edit successfully.')
		else:
			messages.info(self.request, 'Data saved. Nothing has changed')
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		messages.error(request, 'Something is wrong. Edition fails.')
		return super(form_invalid, form)

	def get_success_url(self):
		return reverse('records:patient-detail', kwargs={'id':self.get_object().pk})
