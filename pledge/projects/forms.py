from django import forms

from projects.models import Project

class EditDevelopersForm(forms.ModelForm):
    
    class Meta:
        fields = ('developers',)
        model = Project
        
    
