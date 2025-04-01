from django.urls import path

from accounts.views import (
    forgot_password,
    register_user,
    login_view,
    set_password,
    logout_view,
    show,
)

urlpatterns = [
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("register/", register_user, name="register_user"),
    path("login/", login_view, name="login"),
    path("set-password/<str:token>/", set_password, name="set_password"),
    path("logout/", logout_view, name="logout_view"),
    path("show/", show, name="show"),
]
