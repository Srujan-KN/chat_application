from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'demo/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]