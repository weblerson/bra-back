from .celery import app as celery_app
from typing import Tuple

__all__: Tuple[str, ...] = ('celery_app',)
