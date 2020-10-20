from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
	path('patients',
		views.PatientAllView.as_view(),
		name='patients'),
]