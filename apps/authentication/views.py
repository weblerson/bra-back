from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import PremensActivation, PremensUser
from .forms import CreatePasswordForm


def confirm_register(request: HttpRequest, token):
    activation_token: PremensActivation = get_object_or_404(
        PremensActivation, token=token
    )

    match request.method:
        case 'GET':
            form: CreatePasswordForm = CreatePasswordForm()
            context = {
                'form': form,
                'token': token
            }

            return render(request, 'create_password.html', context)

        case 'POST':
            form: CreatePasswordForm = CreatePasswordForm(request.POST)

            if not form.is_valid():
                context = {
                    'form': form,
                    'token': token
                }

                return render(request, 'create_password.html', context)

            data = form.data

            try:
                user: PremensUser = PremensUser.objects.get(
                    email=activation_token.user.email
                )
                user.is_active = True
                user.set_password(data.get('first_password'))
                
                user.save()

                activation_token.delete()

                context = {
                    'body_message': 'Conta confirmada com sucesso! Já pode fechar esta página.'
                }

                return render(request, 'register.html', context)

            except Exception as e:
                print(f'error: {e}')  

                context = {
                    'body_message': 'Erro interno do sistema.'
                }

                return render(request, 'register.html', context)
