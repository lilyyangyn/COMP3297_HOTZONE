from django.urls import path
from . import views

app_name = 'clustering'

urlpatterns = [
	path('',
		views.ClusterNewView.as_view(),
		name='new'),

]