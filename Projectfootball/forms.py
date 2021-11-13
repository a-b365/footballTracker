from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_char(value):

	result=re.match("^[a-zA-Z]?\D+$",value)

	if result is None:
		raise ValidationError(
			_('%(value)s is not allowed'),
			
			params={'value':value},
			
			)
			
	
class SearchForm(forms.Form):

	search_string=forms.CharField(label=False,max_length=100,validators=[validate_char])

