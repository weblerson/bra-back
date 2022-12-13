from django.contrib import admin
from .models import PremensUser
from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import admin as model_admin


@admin.register(PremensUser)
class PremensUserAdmin(model_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    model = PremensUser

    list_display = ("email", "first_name", "last_name", "is_staff")

    fieldsets = model_admin.UserAdmin.fieldsets + (
        ('Informações Residenciais', {'fields': ('cep',)}),
    )
