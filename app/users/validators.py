import re
from django.core.exceptions import ValidationError



def validation_profile_name(profile_name):

    if re.fullmatch(r'[A-ZА-ЯЁ0-9!?:-].*', profile_name):
        return profile_name
    else:
        raise ValidationError(
            message="не соответствует требованиям: (A-ZА-ЯЁ0-9!?:-)"
        )