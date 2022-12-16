from django.db.models.signals import post_save
from django.dispatch import receiver

from django.conf import settings

from .models import PremensUser, PremensActivation

from utils import Utils
from decouple import config
from hashlib import sha256

from typing import Dict


@receiver(post_save, sender=PremensUser, dispatch_uid='premens_user_identifier')
def send_premens_email(sender, instance, created, **kwargs) -> None:
    if created:
        subject: str = 'BRA - E-mail de Confirmação'
        token: str = sha256(('%s:%s' % (instance.get_full_name(), instance.email)).encode()).hexdigest()
        confirmation_link: str = '%s/auth/confirm/%s' % (config('DOMAIN', cast=str), token)

        try:
            activation: PremensActivation = PremensActivation(user=instance, token=token)
            activation.save()

        except Exception as e:
            print(f'error: {e}')

            return

        context: Dict[str, str] = {
            'full_name': instance.get_full_name(),
            'confirmation_link': confirmation_link
        }

        Utils.send_email(
            settings.REGISTER_TEMPLATE_PATH,
            subject,
            [instance.email],
            **context
        )

        # print('created')

    else:
        subject: str = 'BRA - E-mail de Alteração'
        context: Dict[str, str] = {
            'first_name': instance.first_name
        }

        Utils.send_email(
            settings.UPDATE_TEMPLATE_PATH,
            subject,
            [instance.email],
            **context
        )

        # print('not created')
