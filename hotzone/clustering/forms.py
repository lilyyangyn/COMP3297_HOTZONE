from django import forms

class ClusterCreateForm(forms.Form):
	distanceThres = forms.FloatField(
		label="Distace Threshold",
		required=True,
		initial=200.0,
	)
	timeThres = forms.FloatField(
		label="Time Threshold",
		required=True,
		initial=3.0,
	)
	minSize = forms.IntegerField(
		label="Minimum Cluster Size",
		required=True,
		initial=2,
	)
	
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError(u"You need to fill in all blanks")
		elif self.cleaned_data['timeThres']==0:
			self.add_error('timeThres',"timeThres cannot be zero. Please input valid timeThres.")
			raise forms.ValidationError(u"timeThres cannot be zero. Please input valid timeThres.")
		else:
			cleaned_data = super(ClusterCreateForm, self).clean()
		return cleaned_data
