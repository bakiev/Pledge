from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from accounts.models import Invite, Developer

@receiver(pre_save, sender=Invite)
def handle_pre_save_invite(sender, **kwargs):
    pass
    
@receiver(post_save, sender=Invite)
def handle_post_save_invite(sender, **kwargs):
    subject = render_to_string('accounts/invite_subject.txt', {
            'manager': kwargs['instance'].manager
        }
    )
    content = render_to_string('accounts/invite_content.txt',{
            'key': kwargs['instance'].key,
            'manager': kwargs['instance'].manager
        }
    )
    
    send_mail(subject.replace('\n', ''), content, 
        settings.DEFAULT_FORM_EMAIL, [kwargs['instance'].email,]
    )

