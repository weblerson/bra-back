from django.forms import ModelForm
from django.contrib.auth import forms
from .models import PremensUser

from typing import List


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):

        model = PremensUser


class UserCreationForm(forms.UserCreationForm):

    class Meta(forms.UserCreationForm.Meta):

        model = PremensUser


class PremensUserForm(ModelForm):

    class Meta:
        model: PremensUser = PremensUser
        fields: List[str] = ['first_name', 'last_name', 'cpf', 'cep', 'email', 'password']
