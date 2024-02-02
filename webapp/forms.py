from django.forms import ModelForm
from django import forms
from .models import Brand


class BrandForm(ModelForm):
	class Meta:
		model = Brand
		fields = ['model', 'quality', 'product', 'description', 'price', 'photo']



	