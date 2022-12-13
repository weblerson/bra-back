from django.http import HttpRequest

from decouple import config
from hashlib import sha256

from ninja import Router
from .schemas import User

from .models import PremensUser
from .forms import PremensUserForm

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

    form: PremensUserForm = PremensUserForm(user.dict())
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
                'errors': PremensUser.objects.get(cpf=user.cpf).email
            }

        if PremensUser.objects.filter(email=user.email):
            return {
                'success': False,
                'body': 'Já existe um usuário cadastrado com esse e-mail.',
                'errors': ''
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
