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

	path('forget-password',
		views.ForgetPwdView.as_view(),
		name='forget-pwd'),
	path('reset-password',
		views.ResetPwdView.as_view(),
		name='reset-pwd'),
	path('email-sent',
		views.EmailSentView.as_view(),
		name='email-sent'),
	path('pwd-change-complete',
		views.PwdCompleteView.as_view(),
		name='pwd-complete'),

]