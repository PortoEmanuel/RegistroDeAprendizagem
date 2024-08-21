import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing  # Substitua 'seu_app' pelo nome do seu aplicativo onde 'routing.py' está localizado

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Roteamento padrão para solicitações HTTP
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns  # Aqui deve ser o URLRouter definido em seu routing.py
        )
    ),
})
