from django.urls import path

from accounts.views import forgot_password, register_user

urlpatterns = [
    path("forgot-password/", forgot_password, name="forgot_password"),
    path("register/", register_user, name="register_user"),
]
