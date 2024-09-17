import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from .config import env_vars


async def connect_to_mongo_db():
    uri = env_vars.MONGODB_URL
    client = AsyncIOMotorClient(uri, server_api=ServerApi("1"))

    # GEt DB
    db = client.booknest

    # Get collections
    db = client["user", "book"]

    # send a ping to confirm a successful connection
    try:
        await client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

asyncio.run(connect_to_mongo_db())
