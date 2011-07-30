# -*- coding: utf-8 -*-

from django import forms

from accounts.models import Manager
from projects.models import Project


class ProjectForm(forms.ModelForm):
    manager = forms.ModelChoiceField(queryset=Manager.objects.all())

    class Meta:
        model = Project
