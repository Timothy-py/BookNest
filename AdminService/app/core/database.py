
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from .config import env_vars


client = AsyncIOMotorClient(env_vars.MONGODB_URL, server_api=ServerApi(version="1"))

book_nest_db = client["book_nest_db"]

book_collection = book_nest_db["book_collection"]
user_collection = book_nest_db["user_collection"]
category_collection = book_nest_db["category_collection"]
borrow_book_collection = book_nest_db["borrow_book_collection"]


# Create unique index
async def create_indexs():
    try:
        await category_collection.create_index('title', unique=True)
    except Exception as e:
        print(f"Failed to create index: {e}")

async def connect_to_mongo_db():
    try:
        # send a ping to confirm a successful connection
        await client.admin.command(command="ping")
        await create_indexs()
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


async def close_mongo_db_connection():
    client.close()
    print("Connection to MongoDB closed!")
