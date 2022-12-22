import re
from typing import List

from django.conf import settings
from django.core.mail import BadHeaderError, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Utils:
    @staticmethod
    def send_email(
        template_path: str, subject: str, to: List[str], **kwargs
    ) -> None:
        html_content = render_to_string(template_path, kwargs)
        text_content = strip_tags(html_content)

        try:
            msg = EmailMultiAlternatives(
                subject, text_content, settings.EMAIL_HOST_USER, to
            )
            msg.attach_alternative(html_content, 'text/html')
            msg.send()

        except BadHeaderError:
            print('Invalid header found.')

            return

        return

    @staticmethod
    def validate_password(value: str) -> bool:
        regex: re.Pattern = re.compile(
            r'(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%<^&*?])(?=.*[0-9])[a-zA-Z0-9!@#$%<^&*?]{8,}'
        )
        if not regex.match(value):
            return False

        return True
