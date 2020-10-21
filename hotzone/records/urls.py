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
	path('patient/new',
		views.PatientCreateView.as_view(),
		name='patient-new'),
	path('patient/edit/<int:id>',
		views.PatientEditView.as_view(),
		name='patient-edit'),
	path('patient/delete/<int:id>',
		views.PatientDeleteView.as_view(),
		name='patient-delete'),
]