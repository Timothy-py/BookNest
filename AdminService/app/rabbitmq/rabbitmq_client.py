import json
import asyncio


from aio_pika import Connection, Channel, connect_robust, Message, IncomingMessage

from app.services.borrow_book_service import BorrowBookService
from app.services.user_service import UserService
from app.core.config import env_vars


class RabbitMQClient:
    _instance = None
    
    def __init__(self) -> None:
        self.amqp_url = env_vars.AMQP_URL
        self.connection: Connection = None
        self.channel: Channel = None
        self.consume_task: asyncio.Task = None
        
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    async def connect(self):
        if not self.connection or self.connection.is_closed:
            self.connection = await connect_robust(self.amqp_url)
            self.channel = await self.connection.channel()
        print("RabbitMQ connection established!")
            
    async def publish(self, queue_name: str, message: json):
        await self.connect()
        queue = await self.channel.declare_queue(queue_name, durable=True)
        await self.channel.default_exchange.publish(
            Message(message.encode()),
            routing_key=queue.name
        )
        
    async def on_message(self, message: IncomingMessage):
        async with message.process():
            routing_key = message.routing_key
            data = json.loads(message.body.decode('utf-8'))
            if routing_key == 'user_enroll':
                await UserService.enroll_user(data)
            elif routing_key == 'borrow_book':
                await BorrowBookService.borrow_book(data)
            
    async def consume(self, queue_name: str):
        await self.connect()
        channel = await self.connection.channel()
        queue = await channel.declare_queue(queue_name, durable=True)
        await queue.consume(self.on_message, no_ack=False)
        
    async def start_consume(self, queue_names: list):
        for queue_name in queue_names:
            self.consume_task = asyncio.create_task(self.consume(queue_name))
            
    async def close(self):
        if self.channel:
            await self.channel.close()
        if self.consume_task:
            self.consume_task.cancel()
            try:
                await self.consume_task
            except asyncio.CancelledError:
                pass
            except Exception as e:
                print(e)
        if self.connection:
            await self.connection.close()
        print("RabbitMQ connection closed!")