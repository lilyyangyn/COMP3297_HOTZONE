from django.views.generic import TemplateView, FormView
from ..views import CustomizedListView, CustomizedShowView, CustomizedCreateView, CustomizedEditView, CustomizedDeleteView
from ..models import Location
from ..forms import LocationQueryForm, LocationCreateForm
from django.urls import reverse
import requests
import urllib.parse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LocationAllView(CustomizedListView):
	template_name = "record/location/index.html"
	model = Location

class LocationShowView(CustomizedShowView):
	template_name = "record/location/show.html"
	model = Location
	instanceName = 'location'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

class LocationCreateMainView(TemplateView):
	template_name = "record/location/new.html"

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get(self, request, *args, **kwargs):
		locName = self.request.session.get('query_loc')
		dataList = []
		if request.session.get('data_list'):
			for data in request.session.get('data_list'):
				name = data['nameEN'] if data['nameEN'] else locName
				address = data['addressEN']
				xCoord = data['x']
				yCoord = data['y']
				dataList.append({
					'name': name, 
					'address': address, 
					'XCoord': xCoord, 
					'YCoord': yCoord
				},)
				# assume there is only one returned location result
				break;
		
		context = self.get_context_data(**kwargs)
		context['data_list'] = dataList

		search_form = LocationQueryForm(self.request.GET or None)
		if locName:
			search_form.fields['name'].initial = locName
		context['search_form'] = search_form

		if dataList:
			create_form = LocationCreateForm(request.GET or None)
			context['create_form'] = create_form

		try:
			del request.session['query_loc']
			del request.session['data_list']
		except KeyError:
			pass

		return self.render_to_response(context)

class LocationCreateView(CustomizedCreateView):
	template_name = "record/location/new.html"
	form_class = LocationCreateForm
	model = Location
	success_notice = 'Data saved. Creation successfully.'
	error_notice = 'Something is wrong. Creation fails.'

	def get_success_url(self):
		return reverse('records:location-show', kwargs={'id': self.kwargs['id']})

	def form_valid(self, form):
		submit_location = eval(form.data['location'])
		print(submit_location)
		print(submit_location['name'])
		location = self.model(
				name = submit_location['name'],
				XCoord = submit_location['XCoord'],
				YCoord = submit_location['YCoord'],
			)
		if submit_location['address']:		# query succeeds
			setattr(location, 'address', submit_location['address'])

		location.save()
		self.kwargs['id'] = location.pk

		messages.success(self.request, self.success_notice)
		return HttpResponseRedirect(self.get_success_url())

	def form_invalid(self, form):
		messages.error(self.request, self.error_notice)
		return self.get(self.request)

	def get(self, request, *args, **kwargs):
		return HttpResponseRedirect(reverse('records:location-new'))


class LocationQueryView(FormView):
	template_name = "record/location/new.html"
	form_class = LocationQueryForm
	success_info_notice = "Please select a appropriate location below"
	error_no_reponse_notice = "GeoData does not response."
	error_notice = 'Fail to query GeoData.'

	@method_decorator(login_required)
	def dispatch(self, *args, **kwargs):
		return super().dispatch(*args, **kwargs)

	def get_success_url(self):
		return reverse('records:location-new')

	def form_valid(self, form):
		locName = form.cleaned_data['name']
		locDataList = self.get_query_data(self.get_query_url(locName))
		self.request.session['query_loc'] = locName
		if locDataList:
			self.request.session['data_list'] = locDataList
			messages.info(self.request, self.success_info_notice)
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(reverse('records:location-new'))

	def get_query_data(self, queryUrl):
		attempt_num = 0
		res = requests.get(queryUrl, timeout=5)
		if res.status_code == 200:	# OK
			data = res.json()
			return data
		elif not res:
			messages.error(self.request, self.error_no_reponse_notice)
		else:
			messages.error(self.request, self.error_notice)
		return None

	def get_query_url(self, queryKey):
		encodedKey = urllib.parse.quote(queryKey)
		return "https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=" + encodedKey;

	def get(self, request, *args, **kwargs):
		return HttpResponseRedirect(reverse('records:location-new'))

class LocationDeleteView(CustomizedDeleteView):
	success_message = 'Delete Successfully.'
	model = Location

	def get_success_url(self):
		return reverse('records:locations')