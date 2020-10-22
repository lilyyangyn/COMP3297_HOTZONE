from django.views.generic import ListView
from ..views import CustomizedShowView, CustomizedCreateView, CustomizedEditView, CustomizedDeleteView
from ..models import Location
from django.urls import reverse

class LocationAllView(ListView):
	template_name = "record/location/location_index.html"
	model = Location

class LocationShowView(CustomizedShowView):
	template_name = "record/location/location_show.html"
	model = Location
	instanceName = 'location'

class LocationCreateView(CustomizedCreateView):
	template_name = "record/location/location_new.html"
	model = Location
	fields = '__all__'
	success_notice = 'Data saved. Creation successfully.'
	error_notice = 'Something is wrong. Creation fails.'

	def get_success_url(self):
		return reverse('records:location-show', kwargs={'id': self.kwargs['id']})

class LocationEditView(CustomizedEditView):
	template_name = "record/location/location_edit.html"
	model = Location
	fields = '__all__'
	success_notice_changed = 'Data saved. Edit successfully.'
	success_notice_unchanged = 'Data saved. Nothing has changed'
	error_notice = 'Something is wrong. Edition fails.'

	def get_success_url(self):
		return reverse('records:location-show', kwargs={'id':self.get_object().pk})

class LocationDeleteView(CustomizedDeleteView):
	success_message = 'Delete Successfully.'
	model = Location

	def get_success_url(self):
		return reverse('records:locations')