import os
from .routing import websocket_urlpatterns
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import OriginValidator
from django.core.asgi import get_asgi_application
from .middleware import TokenAuthMiddlewareStack


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'real_estate_portal.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket":
            TokenAuthMiddlewareStack(
                URLRouter(
                websocket_urlpatterns
                )

        ),
    }
)
