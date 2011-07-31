from django.conf.urls.defaults import patterns, include, url

from projects.views import (ProjectCreateView, DeveloperAddView,
                            DeveloperDeleteView, ProjectListView)

urlpatterns = patterns('',
    url(r'^$', ProjectListView.as_view(), name='project_list'),
    url(r'^(?P<pk>\d+)/$', ProjectDetailView.as_view(), name='project_detail'),
    url(r'^create/$', ProjectCreateView.as_view(), name='project_create'),
    url(r'^(?P<pk>\d+)/developer/add/$', DeveloperAddView.as_view(),
        name='developer_add'),
    url(r'^(?P<pk>\d+)/developer/(?P<developer_pk>\d+)/delete/$', DeveloperDeleteView.as_view(),
        name='developer_delete'),
)
