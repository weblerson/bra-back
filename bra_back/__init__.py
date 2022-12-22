from typing import Tuple

from .celery import app as celery_app

__all__: Tuple[str, ...] = ('celery_app',)
