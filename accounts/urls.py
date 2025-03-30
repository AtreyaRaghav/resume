from django.urls import path

from accounts.views import forgot_password

urlpatterns = [
    path("forgot-password/", forgot_password, name="forgot_password"),
]
