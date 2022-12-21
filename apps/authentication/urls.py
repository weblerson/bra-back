from django.urls import path
from . import views

urlpatterns = [
    path('confirm/<str:token>', views.confirm_register, name='confirm_register')
]
