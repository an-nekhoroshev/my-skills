from django.forms import ModelForm
from django import forms
from .models import Links


class LinkForm(ModelForm):

    class Meta:
        model = Links
        widgets = {
            'user': forms.HiddenInput(),
        }
        fields = ['long_link', 'slug', 'name_link', 'user']
