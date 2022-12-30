from typing import List

from django import forms as django_forms
from django.contrib.auth import forms
from django.forms import ModelForm

from .models import PremensUser
from utils import Utils


class UserChangeForm(forms.UserChangeForm):

    class Meta(forms.UserChangeForm.Meta):

        model = PremensUser


class UserCreationForm(forms.UserCreationForm):

    class Meta(forms.UserCreationForm.Meta):

        model = PremensUser


class PremensUserForm(ModelForm):

    class Meta:
        model: PremensUser = PremensUser
        fields: List[str] = [
            'first_name',
            'last_name',
            'cpf',
            'cep',
            'email',
            'password',
        ]


class CreatePasswordForm(django_forms.Form):
    
    first_password = django_forms.CharField(
        widget=django_forms.PasswordInput(),
        required=True,
        min_length=8
        )
    second_password = django_forms.CharField(
        widget=django_forms.PasswordInput(),
        required=True,
        min_length=8
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('first_password').widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields.get('second_password').widget.attrs.update({'class': 'form-control form-control-sm'})

        self.fields.get('first_password').widget.attrs.update({'id': 'first_password'})
        self.fields.get('second_password').widget.attrs.update({'id': 'second_password'})

        self.fields.get('first_password').widget.attrs.update({'name': 'first_password'})
        self.fields.get('second_password').widget.attrs.update({'name': 'second_password'})

    def clean(self):
        super(CreatePasswordForm, self).clean()

        first_password = self.cleaned_data.get('first_password')
        second_password = self.cleaned_data.get('second_password')

        password_message = 'É preciso que sua senha tenha no mínimo uma letra maiúscula, um número e um caractere especial.'

        if not Utils.validate_password(first_password):
            self._errors.update({
                'first_password': self.error_class([password_message])
            })

        if not Utils.validate_password(second_password):
            self._errors.update({
                'second_password': self.error_class([password_message])
            })

        if not first_password == second_password:
            not_match_message = 'As senhas não coincidem.'

            self._errors.update({
                'matches': self.error_class([not_match_message])
            })

        return self.cleaned_data


class CEPForm(django_forms.Form):
    cep = django_forms.CharField(max_length=8)

    def clean(self):
        super(CEPForm, self).clean()

        cep = self.cleaned_data.get('cep').strip()
        if not cep:
            self._errors.update({
                'cep': 'O CEP não pode estar vazio.'
            })

        if len(cep) != 8:
            self._errors.update({
                'cep': 'O CEP precisa ter 8 dígitos!'
            })

        return self.cleaned_data
    