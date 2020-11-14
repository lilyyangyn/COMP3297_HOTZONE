from django.urls import path
from . import views

app_name = 'customauth'

urlpatterns = [
	path('login',
		views.LoginView.as_view(),
		name='login'),

	path('logout',
		views.LogoutView.as_view(),
		name='logout'),
	path('forget_pwd',
	    views.ForgetPwdView.as_view(),
		name='forget_pwd'),
]