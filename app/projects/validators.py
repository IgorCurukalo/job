import re
from django.core.exceptions import ValidationError


def validation_project_name(name):

    if re.fullmatch(r'[A-ZА-ЯЁ0-9!?:-].*', name):
        return name
    else:
        raise ValidationError(
            message="не соответствует требованиям: (A-ZА-ЯЁ0-9!?:-)"
        )