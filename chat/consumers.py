import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Aceita a conexão do WebSocket
        await self.accept()

    async def disconnect(self, close_code):
        # Lida com a desconexão do WebSocket
        pass

    async def receive(self, text_data):
        # Lida com a recepção de mensagens do WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Envia a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))