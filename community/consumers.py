from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import sync_to_async
from .models import Order

class MakeOrder(WebsocketConsumer):
    def connect(self):
        self.user = self.scope['user'].username
        self.room_name = self.scope['route_url']['kwargs']
        async_to_async(self.channel_layer.group_add)(self.channel_name, self.room_name)
        self.accept()

    def disconnect(self, close_code):
         sync_to_async(self.channel_layer.group_discard)(self.channel_name, self.room_name)

    def receive(self, text_data):
        text_message = json.loads(text_data)['message']
        sync_to_async(self.channel_layer.group_send)(self.room_name, {"type": "order", "message": message})
        self.req = Order.objects.create(message=text_message)

    def order(self, event):
        self.send(json.dumps({"message": event['message'], "request_id": self.req.req_id}))

class AcceptRequest(WebsocketConsumer):    
    def connect(self):
        self.user = self.scope['user'].username
        self.room_name = self.scope['route_url']['kwargs']
        async_to_async(self.channel_layer.group_add)(self.channel_name, self.room_name)
        self.accept()

    def disconnect(self, close_code):
         sync_to_async(self.channel_layer.group_discard)(self.channel_name, self.room_name)

    def receive(self, text_data):
        req_id = json.loads(text_data)['request_id']
        sync_to_async(self.channel_layer.group_send)(self.room_name, {"type": "order", "message": self.user + " Has accepted the request"})
        req = Order.objects.get(id=req_id)
        user = User.objects.get(id=self.user)
        Order.user.add(user)

    def order(self, event):
        self.send(json.dumps({"message": event['message']}))

