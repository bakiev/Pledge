# -*- coding: utf-8 -*-

from django.views.generic import CreateView, DeleteView, ListView
from django.core.urlresolvers import reverse

from projects.models import Project, Manager
from projects.forms import ProjectForm
from accounts.models import Developer

class ProjectListView(ListView):
    model = Project


class ProjectCreateView(CreateView):
    model = Project

    def get_success_url(self):
        return reverse('project_list')

    def get_form_class(self):
        # form_class = super(ProjectCreateView, self).get_form_class()
        return ProjectForm

    def get_initial(self):
        initial = super(ProjectCreateView, self).get_initial()
        initial[u'manager'] = Manager.objects.get(user=self.request.user)
        return initial

    def get_form_kwargs(self):
        kwargs = super(ProjectCreateView, self).get_form_kwargs()
        import pdb; pdb.set_trace()
        return kwargs


class DeveloperListView(ListView):
    model = Developer


class DeveloperAddView(CreateView):
    model = Developer
    success_url = '/'


class DeveloperDeleteView(DeleteView):
    model = Developer
