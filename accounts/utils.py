import string
from typing import Tuple
from accounts.models import BlackListEmail


def verify_email(email_str: str) -> Tuple[bool, str]:
    """
    @sarvika.com
    """
    if email_str == "" or email_str is None:
        return False, "Email address cannot be Null or Blank"

    email_object = BlackListEmail.objects.filter(email=email_str).first()

    if email_object is None:
        return False, "Email is in Black List"
    accepted_domains = ["@sarvika.com"]

    for domain in accepted_domains:
        if email_str.endswith(domain):
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
