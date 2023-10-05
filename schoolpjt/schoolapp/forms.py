from .models import Category, Course
from django import forms
class LocationForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.all())