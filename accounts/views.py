from django.shortcuts import redirect, render
from accounts.utils import (
    password_strength,
    verify_email,
    send_email,
    generate_random_string,
)
from django.http import HttpRequest
from accounts.models import User, SetToken, BlackListEmail
from typing import Union


def set_token(email_str: str):
    """ """
    try:
        token: str = generate_random_string()
        token_to_db = SetToken()
        token_to_db.email = email
        token_to_db.token = token
        token_to_db.save()

        return token
    except Exception as e:
        print(e)
        return False


def forgot_password(request):
    """ """
    if request.method == "POST":
        email = request.POST.get("email", "")
        is_valid_email = verify_email(email)

        if not is_valid_email[0]:
            return render(request, "error.html", context={"msg": is_valid_email[1]})

    return render(
        request, "accounts/forgot_password.html", context={"msg": "forgot_password"}
    )


def register_user(request: HttpRequest) -> Union[render, redirect]:
    """"""
    if request.method == "POST":
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        email = request.POST.get("email", "")

        if (
            first_name == ""
            or last_name == ""
            or last_name is None
            or first_name is None
        ):
            return render(
                request,
                "accounts/register.html",
                context={"msg": "first name and last name cannot be none or null"},
            )

        verify_email_str = verify_email(email)
        if not verify_email_str[0]:
            return render(
                request, "accounts/register.html", context={"msg": verify_email_str[1]}
            )

        try:
            token = set_token()

            if not token:
                return "Error While Generating the token retry after some time"

            new_user = User()
            new_user.first_name = first_name
            new_user.last_name = last_name
            new_user.email = email
            new_user.set_unusable_password()
            new_user.full_clean()
            new_user.save()

            send_email(
                subject="email for generating password",
                message=f"{token}",
                email_from="admin@sarvika.com",
                email_to=email,
            )

        except Exception as e:
            print(e)
            return render(request, "accounts/register.html", context={"msg": e})
        return redirect("login")

    return render(request, "accounts/register.html", context={"msg": "hello"})


def login_view(request: HttpRequest) -> render:
    """ """
    if request.method == "POST":

        pass

    return render(
        request, "accounts/login.html", context={"msg": "get request in login"}
    )


def set_password(request: HttpRequest, token: str):
    """ """
    if request.method == "POST":
        pass
    return render(request, "")


def logout_view(request: HttpRequest):
    pass
