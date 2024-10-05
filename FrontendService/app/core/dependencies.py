
from app.rabbitmq.rabbitmq_client import RabbitMQClient


rabbitmq_client = RabbitMQClient()

async def get_rabbitmq_client() -> RabbitMQClient:
    return rabbitmq_client