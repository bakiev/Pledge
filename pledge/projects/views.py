# -*- coding: utf-8 -*-

from django.views.generic import CreateView, UpdateView, DeleteView, ListView,\
    DetailView
from django.core.urlresolvers import reverse

from projects.models import Project, Manager
from projects.forms import EditDevelopersForm
from accounts.models import Developer


class ProjectListView(ListView):
    model = Project


class ProjectDetailView(DetailView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project

    def get_success_url(self):
        return reverse('project_list')

    def get_initial(self):
        '''Set manager
        '''
        initial = super(ProjectCreateView, self).get_initial()
        try:
            initial['manager'] = Manager.objects.get(user=self.request.user.pk)
        except Manager.DoesNotExist:
            pass
        return initial

    def get_form(self, *args, **kwargs):
        '''Hide manager input field
        '''
        form = super(ProjectCreateView, self).get_form(*args, **kwargs)
        form.fields['manager'].widget = form.fields['manager'].hidden_widget()
        return form


class DeveloperListView(ListView):
    model = Developer


class DeveloperAddView(UpdateView):
    model = Project
    form_class = EditDevelopersForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.kwargs['pk']})


class DeveloperDeleteView(DeleteView):
    model = Developer
