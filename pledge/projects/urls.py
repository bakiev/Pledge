from django.conf.urls.defaults import patterns, include, url

from projects.views import (ProjectCreateView, DeveloperAddView,
                            DeveloperDeleteView, ProjectListView)

urlpatterns = patterns('',
    url(r'^$', ProjectListView.as_view(), name='project_list'),
    url(r'^create/$', ProjectCreateView.as_view(), name='project_create'),
    url(r'^(?P<project_id>\d+)/developer/add/$', DeveloperAddView.as_view(),
        name='developer_add'),
    url(r'^(?P<project_id>\d+)/developer/(?P<pk>\d+)/delete/$', DeveloperDeleteView.as_view(),
        name='developer_delete'),
)
