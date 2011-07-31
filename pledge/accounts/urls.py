from django.conf.urls.defaults import patterns, include, url
from django.contrib.auth.decorators import login_required

from accounts import views
from libs.decorators import is_user_is_manager

urlpatterns = patterns('',
    url(r'^send-invite/$', 
        is_user_is_manager(views.InviteFormView.as_view()), 
        {}, 
        'send_invite'
    ),
    url(r'^developers/$',
        is_user_is_manager(views.DevelopersListView.as_view()),
        {},
        'show_developers'
    ),
    url(r'^developer/(?P<pk>\d+)/delete/$',
        is_user_is_manager(views.ExcludeDeveloperView.as_view()),
        {},
        'delete_developer'
    ),
)
