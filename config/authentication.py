
import jwt
from django.conf import settings
from users.models import User
from rest_framework import authentication

class JWTAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.META.get("HTTP_AUTHORIZATION")#WSGIPassAuthorization On
            if token is None:
                return None
            xjwt,jwt_token = token.split(" ")
            decoded = jwt.decode(jwt_token,settings.SECRET_KEY,algorithms=['HS256'])
            #print(decoded)
            pk = decoded.get('pk')
            user = User.objects.get(pk=pk)
            return (user,None)
        except (ValueError,jwt.exceptions.DecodeError,User.DoesNotExist):
            return None