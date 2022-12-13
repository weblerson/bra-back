from django.core.exceptions import ValidationError

import re


def validate_digits(value: str) -> None:
    if not value.isdigit():
        raise ValidationError(
            '%s is not numeric.' % (value,)
        )


def validate_cpf_length(value: str) -> None:
    if len(value) < 11:
        raise ValidationError(
            'CPF length is lower than 11.'
        )


def validate_cep_length(value: str) -> None:
    if len(value) < 8:
        raise ValidationError(
            'CEP length is lower than 8.'
        )


def validate_password(value: str) -> None:
    regex: re.Pattern = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%<^&*?])(?=.*[0-9])[a-zA-Z0-9!@#$%<^&*?]{8,}')
    if not regex.match(value):
        raise ValidationError(
            'Enter a strong password! A strong password is made up of 8 digits and must contain at least 1 number, '
            'an uppercase letter, a lowercase letter and a symbol. '
        )
