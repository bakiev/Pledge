from django.contrib.auth.models import User
from django.contrib.sites.models import RequestSite, Site

from registration import signals
from registration.backends.default import DefaultBackend
from registration.models import RegistrationProfile

from accounts.models import Manager, Developer

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
        user, email = kwargs['username'], kwargs['email']
        password = kwargs['password1']
        
        new_user = self.own_registration(request, user, email, password)
        try:
            invite = kwargs['invite']
            manager_id = kwargs['manager_id']
            new_developer = Developer(user=new_user, manager_id=manager_id)
            new_developer.save()
        except KeyError:
            new_manager = Manager(user=new_user)
            new_manager.save()
        
        return new_user

