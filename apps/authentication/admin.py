from typing import List, Tuple

from django.contrib import admin
from django.contrib.auth import admin as model_admin

from .forms import UserChangeForm, UserCreationForm
from .models import PremensActivation, PremensUser


@admin.register(PremensUser)
class PremensUserAdmin(model_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = PremensUser

    list_display: Tuple[str, ...] = (
        'email',
        'id',
        'first_name',
        'last_name',
        'is_staff',
    )

    fieldsets: Tuple = model_admin.UserAdmin.fieldsets + (
        ('Informações Residenciais', {'fields': ('cep',)}),
        ('Informações Pessoais Extras', {'fields': ('cpf',)}),
    )


@admin.register(PremensActivation)
class PremensUserAdmin(admin.ModelAdmin):

    fieldsets: Tuple = (
        ('Informação Pessoal', {'fields': ('user',)}),
        ('Token de Ativação', {'fields': ('token',)}),
    )

    readonly_fields: List[str] = ['user', 'token']
