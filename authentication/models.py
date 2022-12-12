from django.db import models
from django.contrib.auth.models import AbstractUser


class PremensUser(AbstractUser):

    cep: models.CharField = models.CharField(max_length=8, blank=False)

    def __str__(self) -> str:
        return self.get_full_name()
