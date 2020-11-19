from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'customauth'

urlpatterns = [
	path('login',
		views.LoginView.as_view(),
		name='login'),

	path('logout',
		views.LogoutView.as_view(),
		name='logout'),

]