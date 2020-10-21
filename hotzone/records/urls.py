from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
	path('patients',
		views.PatientAllView.as_view(),
		name='patients'),
	path('patient/<int:id>',
		views.PatientDetailView.as_view(),
		name='patient-detail'),
	path('patient/edit/<int:id>',
		views.PatientEditView.as_view(),
		name='patient-edit'),
]