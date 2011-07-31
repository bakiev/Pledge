# Create your views here.
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from django.shortcuts import redirect

from accounts.forms import InviteForm
from accounts.models import Invite, Manager, Developer

class InviteFormView(CreateView):
    model = Invite
    form_class = InviteForm
    template_name = 'accounts/invite_form.html'
    success_url = '/accounts/sended_invite/'
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.manager = Manager.objects.get(user=self.request.user)
        self.object.save()
        return redirect(self.get_success_url())

class DevelopersListView(ListView):
    template_name = 'accounts/developer_list.html'
    
    def get_queryset(self):
        manager = Manager.objects.get(user=self.request.user)
        return Developer.objects.filter(
            manager=manager
        )

class ExcludeDeveloperView(DeleteView):
    model = Developer
    success_url = '/'
