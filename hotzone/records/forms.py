from django import forms
from .models import Location

class LocationQueryForm(forms.ModelForm):
	class Meta:
		model = Location
		fields = ['name']

class LocationCreateForm(forms.Form):
	def __init__(self, instance, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def is_valid(self):
		location = eval(self.data.get('location'))
		if location['name'] and location['XCoord'] and location['YCoord']:
			return True
		else:
			return False
