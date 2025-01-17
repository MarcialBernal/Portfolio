from django.urls import path
from .views import VRegister, logout, login_view


urlpatterns = [
    path('', VRegister.as_view(), name = "auth"),
    path('logout', logout, name = "logout"),
    path('login', login_view, name = "login"),
]