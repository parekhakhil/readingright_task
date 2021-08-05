from .views import register,profile
from django.urls import path
app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path('accounts/profile/', profile, name='profile'),
]
