from celery import shared_task
from typing import List

from utils import Utils


@shared_task(name='send_email', bind=True, max_retries=5, default_retry_delay=2)
def send_email_task(self, template_path: str, subject: str, to: List[str], **kwargs) -> bool:
    try:
        Utils.send_email(template_path, subject, to, **kwargs)

        return True

    except Exception as e:
        self.retry(countdown=2 * self.request.retries)

        raise Exception(e)
