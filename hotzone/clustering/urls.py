from django.urls import path
from . import views

app_name = 'clustering'

urlpatterns = [
	path('new',
		views.ClusterNewView.as_view(),
		name='new'),

]