from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class CaseInsensitiveModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            # Perform a case-insensitive lookup for the username
            user = UserModel._default_manager.get(**{
                f'{UserModel.USERNAME_FIELD}__iexact': username
            })
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None