from django.contrib.auth.models import User
from django.contrib.sites.models import RequestSite, Site
from django.http import Http404

from registration import signals
from registration.backends.default import DefaultBackend
from registration.models import RegistrationProfile

from accounts.models import Manager, Developer, Invite

class PledgeRegistration(DefaultBackend):
    def own_registration(self, request, user, email, password):
        if  Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)
        
        return RegistrationProfile.objects.create_inactive_user(
            user, email, password, site
        )
        
        
    def register(self, request, **kwargs):
        '''
        regisration of managers and developers(if we have got invite code)
        '''
        user = kwargs['username'] 
        password = kwargs['password1']
        
        is_developer = False
        try:
            key = request.GET['invite']
            invite =  Invite.objects.get(key=key)
            if invite.is_used:
                raise Http404()
            invite.is_user = True
            invite.save()
            
            email = invite.email
            is_developer = True
        except KeyError:
            email = kwargs['email']
            
        new_user = self.own_registration(request, user, email, password)
        if is_developer:
            new_developer = Developer(user=new_user, manager_id=invite.manager_id)
            new_developer.save()
        else:
            new_manager = Manager(user=new_user)
            new_manager.save()
            
        return new_user

