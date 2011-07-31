from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from accounts.forms import DeveloperRegForm

urlpatterns = patterns('',
    url(r'^registration/register/$', 'registration.views.register', {
            'backend': 'accounts.backends.PledgeRegistration',
        }, 'register'),
    url(r'^registration/developer/register/$','registration.views.register', {
            'backend': 'accounts.backends.PledgeRegistration',
            'form_class': DeveloperRegForm
        }, 'developer_register'),
    url(r'^registration/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^project/', include('projects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
