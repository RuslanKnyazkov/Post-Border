from random import choice
from string import digits, ascii_uppercase, ascii_lowercase
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


COLLECTIONS = str(digits + ascii_uppercase + ascii_lowercase)
def generated_code():
    code = ''
    for i in range(6):
        code += choice(COLLECTIONS)
    return code


def validate_unique_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError('Этот адрес электронной почты уже используется.')