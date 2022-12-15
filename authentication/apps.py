from django.apps import AppConfig
from django.core.signals import request_finished


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    def ready(self) -> None:

        from . import signals

        request_finished.connect(signals.send_premens_email)