from django.db import close_old_connections
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from jwt import decode as jwt_decode
from django.conf import settings
from django.contrib.auth import get_user_model
from urllib.parse import parse_qs
from django.contrib.auth.models import AnonymousUser

from channels.db import database_sync_to_async

User=get_user_model()
@database_sync_to_async
def get_user(user_id):
    try:
        return  User.objects.get(id=user_id)
    except User.DoesNotExist:
        return AnonymousUser()

class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner
    def __call__(self, scope):
        return TokenAuthMiddlewareInstance(scope, self)


class TokenAuthMiddlewareInstance:
    def __init__(self, scope, middleware):
        self.middleware = middleware
        self.scope = dict(scope)
        self.inner = self.middleware.inner

    async def __call__(self, receive, send):
        token = parse_qs(self.scope["query_string"].decode("utf8"))["token"][0]

        try:
            UntypedToken(token)

        except (InvalidToken, TokenError) as e:
            # Token is invalid
            # print(e)
            return None
        else:
            decoded_data = jwt_decode(token, settings.SIMPLE_JWT_SIGNING_KEY, algorithms=["HS256"])


        self.scope['user'] = await get_user(decoded_data['user_id'])
        return await self.inner(self.scope, receive, send)




TokenAuthMiddlewareStack = lambda inner: TokenAuthMiddleware(inner)