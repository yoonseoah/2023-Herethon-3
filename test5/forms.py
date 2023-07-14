from django import forms
from .models import RATE_CHOICES, Reviewww
class RateFormmm(forms.ModelForm):
	text = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), required=False)
	rateee = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.Select(), required=True)

	class Meta:
		model = Reviewww
		fields = ('text', 'rateee')
