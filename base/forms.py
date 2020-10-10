from django import forms
from django.forms import ModelForm

from .models import Project, Bio


class ProjectForm(ModelForm):

    class Meta:
        model = Project
        fields = '__all__'

        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }


class BioForm(ModelForm):

    class Meta:
        model = Bio
        fields = '__all__'

        widgets = {
            'softSkill': forms.CheckboxSelectMultiple(),
            'skill': forms.CheckboxSelectMultiple(),
        }