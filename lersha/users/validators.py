from django.core.exceptions import ValidationError
def phone_number_validator(phone_number):
    try:
        phone_number_in_int = int(phone_number)
    except:
        raise ValidationError('Must Be Integers Only')