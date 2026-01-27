from django.core.exceptions import ValidationError
def phone_number_validator(phone_number):
    try:
        phone_number_in_int = int(phone_number)
    except:
        raise ValidationError('Must Be Integers Only')
    else:
        if len(str(phone_number_in_int)) != 9:
            raise ValidationError('Must Be 9 Digits Only Excluding Country Code')