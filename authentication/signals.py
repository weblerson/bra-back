from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import PremensUser


@receiver(post_save, sender=PremensUser, dispatch_uid='premens_user_identifier')
def send_premens_email(sender, instance=None, created=None, **kwargs):
    if created:
        print('E-mail delivered to %s' % (instance.email,))
