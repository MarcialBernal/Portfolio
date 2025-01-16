from django.urls import path
from .views import VRegister, logout


urlpatterns = [
    path('', VRegister.as_view(), name = "auth"),
    path('logout', logout, name = "logout"),
]