import json


from aio_pika import Connection, Channel, connect, Message


class RabbitMQProducer:
    _instance = None
    
    def __init__(self) -> None:
        self.amqp_url = "amqp://guest:guest@localhost:5672"
        self.connection: Connection = None
        self.channel: Channel = None
        
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    async def connect(self):
        if not self.connection:
            self.connection = await connect(self.amqp_url)
            self.channel = await self.connection.channel()
        print("RabbitMQ connection established!")
            
    async def publish(self, queue_name: str, message: json):
        await self.connect()
        queue = await self.channel.declare_queue(queue_name)
        await self.channel.default_exchange.publish(
            Message(message.encode()),
            routing_key=queue.name
        )
        
    async def close(self):
        if self.channel:
            await self.channel.close()
        if self.connection:
            await self.connection.close()
        print("RabbitMQ connection closed!")