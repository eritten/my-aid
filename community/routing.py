from django.urls import path
from .consumers import MakeOrder

websocket_url_patterns = [path('order/', MakeOrder.as_asgi(), name='order')]
