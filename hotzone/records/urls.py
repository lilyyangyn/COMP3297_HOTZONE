from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
	# path('patients',
	# 	views.PatientAllView.as_view(),
	# 	name='patients'),
	# path('patient/<int:id>',
	# 	views.PatientShowView.as_view(),
	# 	name='patient-show'),
	# path('patient/new',
	# 	views.PatientCreateView.as_view(),
	# 	name='patient-new'),
	# path('patient/edit/<int:id>',
	# 	views.PatientEditView.as_view(),
	# 	name='patient-edit'),
	# path('patient/delete/<int:id>',
	# 	views.PatientDeleteView.as_view(),
	# 	name='patient-delete'),

	path('locations',
		views.LocationAllView.as_view(),
		name='locations'),
	path('location/<int:id>',
		views.LocationShowView.as_view(),
		name='location-show'),
	path('location/new',
		views.LocationCreateMainView.as_view(),
		name='location-new'),
	path('location/query',
		views.LocationQueryView.as_view(),
		name='location-query'),
	path('location/create',
		views.LocationCreateView.as_view(),
		name='location-create'),
	path('location/delete/<int:id>',
		views.LocationDeleteView.as_view(),
		name='location-delete'),
]