from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing

class ThingForm(forms.ModelForm):
	class Meta:
		model = Thing
		fields = ['name','description','quantity']
		widgets = {'description' : forms.Textarea()}

