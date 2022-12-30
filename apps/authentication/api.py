from authentication.forms import PremensUserForm, CEPForm
from authentication.models import PremensUser
from authentication.schemas import Token, CEP
from decouple import config
from django.http import HttpRequest
from django.shortcuts import get_object_or_404
from ninja import Router

import jwt
from entities import User

from utils import Utils

auth_router: Router = Router()



@auth_router.patch('')
def change_cep(request: HttpRequest, cep: CEP):
    payload = jwt.decode(cep.token, config('BRAAuth', cast=str), algorithms=['HS256'])
    user = get_object_or_404(PremensUser, id=payload.get('id'))

    if not user.is_active:
        return {
            'success': False,
            'body': "O usuário não ativou a conta. Impossível realizar a alteração."
        }

    if payload.get('cep') == user.cep:
        return {
            'success': False,
            'body': 'O CEP informado é igual ao CEP registrado. Impossível realizar a alteração.'
        }

    form: CEPForm = CEPForm({'cep': payload.get('cep')})
    if not form.is_valid():
        return {
            'success': False,
            'body': form.errors
        }

    try:
        user.cep = payload.get('cep')
        user.save()

        return {
            'success': True,
            'body': 'CEP alterado com sucesso. Aguarde um e-mail confirmando a alteração.'
        }

    except Exception as e:
        print(e)

        return {
            'success': False,
            'body': e
        }


@auth_router.post('')
def register(request: HttpRequest, token: Token):
    payload = jwt.decode(token.token, config('BRAAuth', cast=str), algorithms=['HS256'])
    user: User = Utils.generate_user(payload)

    if not Utils.validate_password(user.password):
        return {
            'success': False,
            'body': 'A strong password is made up of 8 digits and must contain at least 1 '
            'number, an uppercase letter, a lowercase letter and a symbol. ',
        }

    form: PremensUserForm = PremensUserForm(user.to_json())
    if not form.is_valid():
        errors = form.errors

        return {'success': False, 'body': errors}

    try:
        if PremensUser.objects.filter(cpf=user.cpf):
            return {
                'success': False,
                'body': 'Já existe um usuário com esse CPF cadastrado.',
            }

        if PremensUser.objects.filter(email=user.email):
            return {
                'success': False,
                'body': 'Já existe um usuário cadastrado com esse e-mail.',
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
                is_active=False,
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
                is_staff=True,
            )

        return {'success': True, 'body': 'Usuário cadastrado com sucesso!'}

    except Exception as e:
        return {'success': False, 'body': e}
