from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing

class ThingForm(forms.Form):

	name = forms.CharField(
		label = 'Name',
		max_length = 35)

	description = forms.CharField(
		label = 'Description',
		widget = forms.Textarea(),
		max_length=120)

	quantity = forms.CharField(
		label='Quantity',
		widget = forms.NumberInput(),
		validators = [[MinValueValidator(0),MaxValueValidator(50)]])
