from django.conf.urls.defaults import patterns, include, url

from projects.views import ProjectCreateView, DeveloperAddView

urlpatterns = patterns('',
    url(r'^create/', ProjectCreateView.as_view(), name='project_create'),
    url(r'^(?P<project_id>)/developer/add/', DeveloperAddView.as_view(),
        name='developer_add'),
)

