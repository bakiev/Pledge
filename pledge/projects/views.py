# -*- coding: utf-8 -*-

from django.views.generic import CreateView

from projects.models import Project
from accounts.models import Developer

class ProjectCreateView(CreateView):
    model = Project


class DeveloperAddView(CreateView):
    model = Developer
