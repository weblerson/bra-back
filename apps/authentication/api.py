from django.http import HttpRequest

from decouple import config
from hashlib import sha256

from ninja import Router
from .schemas import User

from .models import PremensUser
from .forms import ValidationForm

auth_router: Router = Router()


@auth_router.post('')
def register(request: HttpRequest, user: User):
    hash_pass = sha256(request.headers.get('BRAAuth').encode()).hexdigest()
    if not hash_pass == config('BRAAuth', cast=str):
        return {
            'success': False,
            'body': 'Senha de acesso incorreta!',
            'errors': ''
        }

    form: ValidationForm = ValidationForm(request.POST)
    if not form.is_valid():
        errors = form.errors

        return {
            'success': False,
            'body': 'Preencha as informações corretamente!',
            'errors': errors
        }

    try:
        if PremensUser.objects.filter(cpf=user.cpf):
            return {
                'success': False,
                'body': 'Já existe um usuário com esse CPF cadastrado.',
                'errors': ''
            }

        if PremensUser.objects.filter(email=user.email):
            return {
                'success': False,
                'body': 'Já existe um usu[ario cadastrado com esse e-mail.',
                'errors': ''
            }

        premens_user: PremensUser = PremensUser(
            first_name=user.first_name,
            last_name=user.last_name,
            cpf=user.cpf,
            cep=user.cep,
            email=user.email
        )

        premens_user.save()

        return {
            'success': True,
            'body': 'Usuário cadastrado com sucesso!',
            'errors': ''
        }

    except Exception as e:
        return {
            'success': False,
            'body': e,
            'errors': ''
        }
