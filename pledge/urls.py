from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pledge.views.home', name='home'),
    # url(r'^pledge/', include('pledge.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', 'registration.views.register', {
            'backend': 'accounts.backends.PledgeRegistration',
        }, 'register'),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
