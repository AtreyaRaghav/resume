from django.shortcuts import render
from accounts.utils import password_strength, verify_email


def forgot_password(request):
    """ """
    if request.method == "POST":
        email = request.POST.get("email", "")
        is_valid_email = verify_email(email)

        if not is_valid_email[0]:
            return render(request, "error.html", context={"msg": is_valid_email[1]})
