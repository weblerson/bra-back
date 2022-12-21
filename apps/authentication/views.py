from typing import Dict

from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import PremensActivation, PremensUser


def confirm_register(request: HttpRequest, token: str):
    _activation_token: PremensActivation = get_object_or_404(
        PremensActivation, token=token
    )

    match request.method:
        case 'GET':
            try:
                user: PremensUser = PremensUser.objects.get(
                    email=_activation_token.user.email
                )
                user.is_active = True

                user.save()

                _activation_token.delete()

                context: Dict[str, str] = {
                    'body_message': 'Conta confirmada com sucesso! Já pode fechar esta página.'
                }

                return render(request, 'register.html', context)

            except Exception as e:
                print(f'error: {e}')

                context: Dict[str, str] = {
                    'body_message': 'Erro interno do sistema.'
                }

                return render(request, 'register.html', context)
