import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter
from community.routing import websocket_url_patterns


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myaid.settings')

application = ProtocolTypeRouter({"http": get_asgi_application(), "websocket": websocket_url_patterns}
)