from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class PremensUser(AbstractUser):

    username: models.CharField = models.CharField(max_length=150, blank=True, default='_')
    email: models.EmailField = models.EmailField(unique=True)

    cep: models.CharField = models.CharField(max_length=8, blank=False)
    cpf: models.CharField = models.CharField(max_length=11, unique=True)

    USERNAME_FIELD: str = 'email'
    EMAIL_FIELD: str = 'email'

    REQUIRED_FIELDS = list()

    objects: UserManager = UserManager()

    def __str__(self) -> str:
        return '%s' % (self.get_full_name())
