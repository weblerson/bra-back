from django.contrib.auth import forms
from .models import PremensUser


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):

        model = PremensUser


class UserCreationForm(forms.UserCreationForm):

    class Meta(forms.UserCreationForm.Meta):

        model = PremensUser
