from django import forms as django_forms
from django.contrib.auth import forms
from .models import PremensUser


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):

        model = PremensUser


class UserCreationForm(forms.UserCreationForm):

    class Meta(forms.UserCreationForm.Meta):

        model = PremensUser


class ValidationForm(django_forms.Form):
    first_name: django_forms.CharField()
    last_name: django_forms.CharField()
    cpf: django_forms.CharField(min_length=11, max_length=11)
    cep: django_forms.CharField(min_length=8, max_length=8)
    email: django_forms.EmailField()
