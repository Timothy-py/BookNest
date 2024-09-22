

from sqlalchemy.ext.asyncio import AsyncSession


from app.core.database import get_session
from app.rabbitmq.rabbitmq_client import RabbitMQClient


rabbitmq_client = RabbitMQClient()

async def get_rabbitmq_client() -> RabbitMQClient:
    return rabbitmq_client

async def get_db_sesssion() -> AsyncSession:
    return await get_session()