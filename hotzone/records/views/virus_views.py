from ..views import CustomizedListView, CustomizedShowView, CustomizedCreateView, CustomizedEditView, CustomizedDeleteView
from ..models import Virus
from django.urls import reverse

class VirusAllView(CustomizedListView):
	template_name = "record/virus/index.html"
	model = Virus

	def get_filters(self):
		filters = {}
		name = self.request.GET.get('qname')
		if name:
			filters['name'] = name.strip()
		return filters

class VirusShowView(CustomizedShowView):
	template_name = "record/virus/show.html"
	model = Virus
	instanceName = 'virus'

class VirusCreateView(CustomizedCreateView):
	template_name = "record/virus/new.html"
	model = Virus
	fields = '__all__'
	success_notice = 'Data saved. Creation successfully.'
	error_notice = 'Something is wrong. Creation fails.'

	def get_success_url(self):
		return reverse('records:virus-show', kwargs={'id': self.kwargs['id']})

class VirusEditView(CustomizedEditView):
	template_name = "record/virus/edit.html"
	model = Virus
	fields = '__all__'
	success_notice_changed = 'Data saved. Edit successfully.'
	success_notice_unchanged = 'Data saved. Nothing has changed'
	error_notice = 'Something is wrong. Edition fails.'

	def get_success_url(self):
		return reverse('records:virus-show', kwargs={'id':self.get_object().pk})

class VirusDeleteView(CustomizedDeleteView):
	success_message = 'Delete Successfully.'
	model = Virus

	def get_success_url(self):
		return reverse('records:viruses')
