from django.contrib import admin
from .models import PremensUser, PremensActivation
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import admin as model_admin

from typing import Tuple, List


@admin.register(PremensUser)
class PremensUserAdmin(model_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = PremensUser

    list_display: Tuple[str, ...] = ("email", "first_name", "last_name", "is_staff")

    fieldsets: Tuple = model_admin.UserAdmin.fieldsets + (
        ('Informações Residenciais', {'fields': ('cep',)}),
        ('Informações Pessoais Extras', {'fields': ('cpf',)})
    )


@admin.register(PremensActivation)
class PremensUserAdmin(admin.ModelAdmin):

    fieldsets: Tuple = (
        ('Informação Pessoal', {'fields': ('user',)}),
        ('Token de Ativação', {'fields': ('token',)})
    )

    readonly_fields: List[str] = ['user', 'token']
