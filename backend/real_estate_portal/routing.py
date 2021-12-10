from django.urls import path,include
from realtimeapp.consumers import RealTimeFunction

websocket_urlpatterns = [
    path('ws/realtime/', RealTimeFunction.as_asgi()),
]
