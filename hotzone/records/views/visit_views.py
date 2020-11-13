from ..views import CustomizedListView, CustomizedShowView, CustomizedCreateView, CustomizedEditView, CustomizedDeleteView
from ..models import Visit, Case
from django.urls import reverse
from django.shortcuts import get_object_or_404

class VisitAllView(CustomizedListView):
	template_name = "record/visit/index.html"
	model = Visit
	case = None

	def get_case(self):
		if not self.case:
			self.case = get_object_or_404(Case, pk = self.kwargs['case'])
		return self.case

	def get_filters(self):
		filters = {}
		filters['case'] = self.get_case()
		dateFrom = self.request.GET.get('qdatefr')
		if dateFrom:
			filters['dateFrom__gte'] = dateFrom.strip()
			filters['dateTo__lte'] = dateFrom.strip()
		dateTo = self.request.GET.get('qdateto')
		if dateTo:
			filters['dateFrom__lte'] = dateTo.strip()
			filters['dateTo__gte'] = dateTo.strip()
		return filters

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['case'] = self.get_case()
		return context

class VisitShowView(CustomizedShowView):
	template_name = "record/visit/show.html"
	model = Visit
	instanceName = 'visit'

class VisitCreateView(CustomizedCreateView):
	template_name = "record/visit/new.html"
	model = Visit
	fields = '__all__'

	def get_initial(self):
	    initial = super().get_initial()
	    initial = initial.copy()
	    initial['case'] = self.kwargs['case']
	    return initial

	def get_success_url(self):
		return reverse('records:visit-show', kwargs={'id': self.kwargs['id']})

	def get_form(self):
		form = super().get_form(self.get_form_class())
		form.fields['case'].queryset = Case.objects.filter(pk=self.kwargs['case'])
		return form

class VisitEditView(CustomizedEditView):
	template_name = "record/visit/edit.html"
	model = Visit
	fields = '__all__'

	def get_success_url(self):
		return reverse('records:visit-show', kwargs={'id':self.get_object().pk})

class VisitDeleteView(CustomizedDeleteView):
	model = Visit

	def get_success_url(self):
		return reverse('records:visits')
