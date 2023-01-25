from django.urls import path
from .consumers import Order

websocket_url_patterns = [path('order/', Order.as_asgi(), name='order')]
