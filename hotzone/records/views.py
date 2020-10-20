from django.views.generic import TemplateView, ListView
from .models import Patient, Virus, Location, Case, Visit

class PatientAllView(ListView):
	template_name = "record/patient_index.html"
	model = Patient

class PatientEditionView(TemplateView):
	template_name = "record/patient_edit.html"
	def get_context_data(self, **kwargs):
		patientName = self.kwargs['name']

		context = super().get_context_data(**kwargs)
		context['patient'] = Patient.objects.get(name=patientName)
		return context