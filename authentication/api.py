from django.http import HttpRequest

from decouple import config
from hashlib import sha256

from ninja import Router
from .schemas import User

from utils import Utils

from .models import PremensUser
from .forms import PremensUserForm

auth_router: Router = Router()


@auth_router.post('')
def register(request: HttpRequest, user: User):
    if not Utils.validate_password(user.password):
        return {
            'success': False,
            'body': 'Enter a strong password! A strong password is made up of 8 digits and must contain at least 1 '
                    'number, an uppercase letter, a lowercase letter and a symbol. '
        }

    hash_pass = sha256(request.headers.get('BRAAuth').encode()).hexdigest()
    if not hash_pass == config('BRAAuth', cast=str):
        return {
            'success': False,
            'body': 'Senha de acesso incorreta!'
        }

    form: PremensUserForm = PremensUserForm(user.dict())
    if not form.is_valid():
        errors = form.errors

        return {
            'success': False,
            'body': errors
        }

    try:
        if PremensUser.objects.filter(cpf=user.cpf):
            return {
                'success': False,
                'body': 'Já existe um usuário com esse CPF cadastrado.'
            }

        if PremensUser.objects.filter(email=user.email):
            return {
                'success': False,
                'body': 'Já existe um usuário cadastrado com esse e-mail.'
            }

        premens_user: PremensUser

        if not user.staff:
            premens_user = PremensUser.objects.create_user(
                first_name=user.first_name,
                last_name=user.last_name,
                cpf=user.cpf,
                cep=user.cep,
                email=user.email,
                password=user.password,
                is_active=False
            )

        else:
            premens_user = PremensUser.objects.create_user(
                first_name=user.first_name,
                last_name=user.last_name,
                cpf=user.cpf,
                cep=user.cep,
                email=user.email,
                password=user.password,
                is_active=False,
                is_staff=True
            )

        # premens_user.save()

        return {
            'success': True,
            'body': 'Usuário cadastrado com sucesso!'
        }

    except Exception as e:
        return {
            'success': False,
            'body': e
        }
