from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required

from accounts.views import InviteFormView

urlpatterns = patterns('',
    url(r'^send-invite/$', 
        login_required(InviteFormView.as_view()), 
        {}, 
        'send_invite'
    ),
    
)
