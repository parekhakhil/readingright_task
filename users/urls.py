from .views import register,profile
from django.urls import path
from django.contrib.auth import views as auth_view
app_name = "users"

urlpatterns = [
    path("register/", register, name="register"),
    path('login/',auth_view.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('accounts/profile/', profile, name='profile'),
]
