from django.views.generic import ListView
from ..views import CustomizedShowView, CustomizedCreateView, CustomizedEditView, CustomizedDeleteView
from ..models import Location
from django.urls import reverse
import requests
import time
from django.contrib import messages
from django.http import HttpResponseRedirect

class LocationAllView(ListView):
	template_name = "record/location/index.html"
	model = Location

class LocationShowView(CustomizedShowView):
	template_name = "record/location/show.html"
	model = Location
	instanceName = 'location'

class LocationCreateView(CustomizedCreateView):
	template_name = "record/location/new.html"
	model = Location
	fields = ['name']
	success_notice = 'Data saved. Creation successfully.'
	error_notice = 'Something is wrong. Creation fails.'
	api_error_notice = 'Fail to find a matched place.'

	max_retries = 5		# max times of query to GeoData retry

	def get_success_url(self):
		return reverse('records:location-show', kwargs={'id': self.kwargs['id']})

	def form_valid(self, form):
		locName = form.cleaned_data['name']
		locDataList = self.get_query_data(self.get_query_url(locName))
		if locDataList and locDataList != None:		# query succeeds
			locData = locDataList[0]
			location = self.model(
				name = locName,
				XCoord = locData['x'],
				YCoord = locData['y']
			)
			if locData['addressEN']:
				setattr(location, 'address', locData['addressEN'])

			location.save()

			self.kwargs['id'] = location.pk

			messages.success(self.request, self.success_notice)
		else:
			messages.error(self.request, self.api_error_notice)
		return HttpResponseRedirect(self.get_success_url())

	def get_query_data(self, queryUrl):
		attempt_num = 0
		while attempt_num < self.max_retries:
			res = requests.get(queryUrl)
			if res.status_code == 200:	# OK
				data = res.json()
				return data
			else:
				attempt_num += 1
				time.sleep(4)	# sleep 4s before retry
		return None


	def get_query_url(self, queryKey):
		return "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=" + queryKey;


class LocationDeleteView(CustomizedDeleteView):
	success_message = 'Delete Successfully.'
	model = Location

	def get_success_url(self):
		return reverse('records:locations')