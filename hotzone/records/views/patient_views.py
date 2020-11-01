from ..views import CustomizedListView, CustomizedShowView, CustomizedCreateView, CustomizedEditView, CustomizedDeleteView
from ..models import Patient
from django.urls import reverse

class PatientAllView(CustomizedListView):
	template_name = "record/patient/index.html"
	model = Patient

class PatientShowView(CustomizedShowView):
	template_name = "record/patient/show.html"
	model = Patient
	instanceName = 'patient'

class PatientCreateView(CustomizedCreateView):
	template_name = "record/patient/new.html"
	model = Patient
	fields = '__all__'
	success_notice = 'Data saved. Creation successfully.'
	error_notice = 'Something is wrong. Creation fails.'

	def get_success_url(self):
		return reverse('records:patient-show', kwargs={'id': self.kwargs['id']})

class PatientEditView(CustomizedEditView):
	template_name = "record/patient/edit.html"
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