import string
from typing import Tuple
from accounts.models import BlackListEmail
from django.core.mail import send_mail
from django.contrib.auth.models import BaseUserManager

import secrets
import string
import inspect


def generate_random_string(length=80) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def verify_email(email_str: str) -> Tuple[bool, str]:
    """
    @sarvika.com
    """
    caller = inspect.stack()[1]
    print(email_str)
    print(f"Called from function: {caller.function}")

    if email_str == "" or email_str is None:
        return False, "Email address cannot be Null or Blank"

    try:
        email_str = BaseUserManager().normalize_email(email_str)
    except Exception as e:
        return False, f"{str(e)}"

    email_object = BlackListEmail.objects.filter(email=email_str).first()

    if email_object is not None:
        return False, "Email is in Black List, Please contact Administrator"

    accepted_domains = ["@sarvika.com"]

    for domain in accepted_domains:
        # email is in accepted domain list and it length should be greater than domains length
        # malicious user may submit only the domain name
        print("Interation in domain")
        if email_str.endswith(domain) and len(email_str) > len(domain):
            return True, "Accepted"

    return False, "Email address is not acceptable"


def password_strength(password_str: str) -> Tuple[bool, str]:
    """
    password length should be greater than 8 charcter
    contains atleast one digit, one lowercase, one uppercase and one special character
    """
    found_digit = False
    found_lowercase = False
    found_uppercase = False
    found_specialcase = False

    if len(password_str) < 8:
        return False, "Password Length should be greater or equal than 8 character"

    for character in password_str:
        if character in string.ascii_uppercase:
            found_uppercase = True
        elif character in string.ascii_lowercase:
            found_lowercase = True
        elif character in string.digits:
            found_digit = True
        elif character in string.punctuation:
            found_specialcase = True
        else:
            return False, "Password should not contain white spaces"

    if (
        not found_uppercase
        or not found_specialcase
        or not found_digit
        or not found_lowercase
    ):
        return True, "Password is not strong"

    return True, "Password is Strong"


def send_email(
    subject: str,
    message: str,
    email_from: str,
    email_to: str,
) -> Tuple[bool, str]:
    """ """
    verify_email_sender = verify_email(email_from)
    if not verify_email_sender[0]:
        return verify_email_sender

    verify_email_receiver = verify_email(email_to)
    if not verify_email_sender[0]:
        return verify_email_receiver

    if message == "" or message is None:
        return False, "Message cannot be null or blank"

    if subject == "" or subject is None:
        return False, "Subject cannot be null or blank"

    email_send_flag = False
    email_send_msg = ""
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=email_from,
            recipient_list=[email_to],
            fail_silently=False,
        )
        email_send_flag = True
        email_send_msg = "Email send"
    except Exception as e:
        print(str(e))
        email_send_flag = False
        email_send_msg = str(e)

    return email_send_flag, email_send_msg


if __name__ == "__main__":
    print(
        send_email(
            subject="first email",
            message="first message",
            email_from="raghav.atreya@sarvika.com",
            email_to="pawan.nagarwal@sarvika.com",
        )
    )
