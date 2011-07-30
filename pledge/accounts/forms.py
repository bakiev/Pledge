from django import forms

from accounts.models import Invite, Developer


class InviteForm(forms.ModelForm):
    class Meta:
        model = Invite
        exclude = ('key', 'manager')
        
