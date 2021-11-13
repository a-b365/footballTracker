from django import forms
from django.utils.translation import gettext as _

class DateInput(forms.DateInput):
	input_type='date'
		
class DateForm(forms.Form):
	date_published=forms.DateField(widget=DateInput,label=_("Choose the preferred news date (required, from 2021 April 1 to June 14)"))