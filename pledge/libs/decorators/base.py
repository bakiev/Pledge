from django.contrib.auth.decorators import user_passes_test

from accounts.models import Manager, Developer

def check_user(user_class, user):
    ret_val = False 
    if user.is_authenticated():
        try:
            is_user = user_class.objects.get(user=user)
            ret_val = True
        except user_class.DoesNotExist:
            pass
    
    return ret_val
    
is_user_is_manager = user_passes_test(
    lambda u: check_user(Manager, u),
    login_url='/forbiden/',
    redirect_field_name=''
)

is_user_is_developer = user_passes_test(
    lambda u: check_user(Developoer, u),
    login_url='/forbiden/',
    redirect_field_name=''
)
