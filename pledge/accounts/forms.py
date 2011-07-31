from django import forms
from django.contrib.auth.models import User

from accounts.models import Invite, Developer



class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        exclude = ('key', 'manager')

class DeveloperRegForm(forms.Form):
    username = forms.CharField(max_length=30, label='username')
    password1 = forms.CharField(max_length=30, label='Password',
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(max_length=30, label='Re password',
        widget=forms.PasswordInput()
    )
    
    def clean_username(self):
        try:
            user = User.objects.get(username__exact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError('The user with that user name exists')
    
    def clean(self):
        if 'password1' in self.cleaned_data and 'passowrd2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError('The two passwords fields didn\'t match')
            
        return self.cleaned_data
