from django.contrib import admin
from .models import PremensUser
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import admin as model_admin


@admin.register(PremensUser)
class PremensUserAdmin(model_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = PremensUser

    fieldsets = model_admin.UserAdmin.fieldsets + (
        ('Informações Residenciais', {'fields': ('cep',)}),
    )
