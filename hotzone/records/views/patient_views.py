from ..views import CustomizedListView, CustomizedShowView, CustomizedCreateView, CustomizedEditView, CustomizedDeleteView
from ..models import Patient
from django.urls import reverse

class PatientAllView(CustomizedListView):
	template_name = "record/patient/index.html"
	model = Patient

	def get_filters(self):
		filters = {}
		name = self.request.GET.get('qname')
		if name:
			filters['name'] = name.strip()
		identity = self.request.GET.get('qid')
		if identity:
			filters['identity'] = identity.strip()
		return filters

class PatientShowView(CustomizedShowView):
	template_name = "record/patient/show.html"
	model = Patient
	instanceName = 'patient'

class PatientCreateView(CustomizedCreateView):
	template_name = "record/patient/new.html"
	model = Patient
	fields = '__all__'

	def get_success_url(self):
		return reverse('records:patient-show', kwargs={'id': self.kwargs['id']})

class PatientEditView(CustomizedEditView):
	template_name = "record/patient/edit.html"
	model = Patient
	fields = '__all__'

	def get_success_url(self):
		return reverse('records:patient-show', kwargs={'id':self.get_object().pk})

class PatientDeleteView(CustomizedDeleteView):
	model = Patient

	def get_success_url(self):
		return reverse('records:patients')