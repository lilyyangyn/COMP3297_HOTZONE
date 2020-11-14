from ..views import CustomizedListView, CustomizedShowView, CustomizedCreateView, CustomizedEditView, CustomizedDeleteView
from ..models import Case
from django.urls import reverse

class CaseAllView(CustomizedListView):
	template_name = "record/case/index.html"
	model = Case

	def get_filters(self):
		filters = {}
		caseNumber = self.request.GET.get('qcaseid')
		if caseNumber:
			filters['caseNumber'] = caseNumber.strip()
		return filters

class CaseShowView(CustomizedShowView):
	template_name = "record/case/show.html"
	model = Case
	instanceName = 'case'

class CaseCreateView(CustomizedCreateView):
	template_name = "record/case/new.html"
	model = Case
	fields = '__all__'

	def get_success_url(self):
		return reverse('records:case-show', kwargs={'id': self.kwargs['id']})

class CaseEditView(CustomizedEditView):
	template_name = "record/case/edit.html"
	model = Case
	fields = '__all__'

	def get_success_url(self):
		return reverse('records:case-show', kwargs={'id':self.get_object().pk})

class CaseDeleteView(CustomizedDeleteView):
	model = Case

	def get_success_url(self):
		return reverse('records:cases')
