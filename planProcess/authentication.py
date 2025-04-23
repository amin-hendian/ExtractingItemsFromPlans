from rest_framework import authentication, exceptions
from rest_framework.request import Request

from core.models import User


class UserAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request: Request):
        api_key = request.headers.get("Authorization")
        if not api_key:
            return None
        try:
            user = User.objects.get(api_key=api_key)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed("No such user")
        return (user, None)
