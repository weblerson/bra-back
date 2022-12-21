from django.core.exceptions import ValidationError


def validate_digits(value: str) -> None:
    if not value.isdigit():
        raise ValidationError('%s is not numeric.' % (value,))


def validate_cpf_length(value: str) -> None:
    if len(value) < 11:
        raise ValidationError('CPF length is lower than 11.')


def validate_cep_length(value: str) -> None:
    if len(value) < 8:
        raise ValidationError('CEP length is lower than 8.')
