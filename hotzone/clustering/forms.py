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