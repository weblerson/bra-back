from django.contrib import admin
from django.urls import path, include

from .api import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('api/v1/', api.urls)
]
