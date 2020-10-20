from django.urls import path
from . import views

urlpatterns = [
	path('patients',
		views.PatientAllView.as_view(),
		name='patients'),
]