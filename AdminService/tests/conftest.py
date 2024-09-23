import asyncio
import pytest
from mongomock_motor import AsyncMongoMockClient


@pytest.fixture(scope="session")
def event_loop():
    """Create an event loop for the session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
async def mock_mongo_client():
    client = AsyncMongoMockClient()
    yield client
    await client.drop_database('book_nest_db')
    

@pytest.fixture
async def mock_book_collection(mock_mongo_client):
    # Mock MongoDB Collection
    db = mock_mongo_client["book_nest_db"]
    collection = db["book_collection"]
    return collection
