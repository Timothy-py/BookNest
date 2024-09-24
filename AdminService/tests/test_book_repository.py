import asyncio
from datetime import date
import uuid
from bson import ObjectId
import pytest
from mongomock_motor import AsyncMongoMockClient


from app.core.database import book_collection
from app.repositories.book_repository import BookRepository


book_id_obj = ObjectId()
book_id_str = str(book_id_obj)
universal_id = str(uuid.uuid4())
book_one = {
        "_id": book_id_obj,
        "universal_id": universal_id,
        "title": "Test Book",
        "author": "John Doe",
        "publisher": "Test Publisher",
        "is_available": True,
        "available_date": None
    }
book_two = {
        "_id": ObjectId(),
        "universal_id": str(uuid.uuid4()),
        "title": "Women of Owu",
        "author": "Femi Osofisan",
        "publisher": "University Press",
        "is_available": True,
        "available_date": None
    }

@pytest.mark.asyncio
async def test_add_book(mock_book_collection):
    new_book = await BookRepository.add_book(book_one)
    await BookRepository.add_book(book_two)
    
    assert new_book.inserted_id is not None    


@pytest.mark.asyncio
async def test_get_book_by_id(mock_book_collection):
    found_book = await BookRepository.get_book_by_id(book_id_str)

    assert found_book is not None
    assert found_book["title"] == "Test Book"


# test_get_book_by_universal_id
@pytest.mark.asyncio
async def test_get_book_by_universal_id(mock_book_collection):
    found_book = await BookRepository.get_book_by_universal_id("1234")

    assert found_book is not None
    assert found_book["author"] == "John Doe"

# test update book availability
@pytest.mark.asyncio
async def test_update_book_availability(mock_book_collection):
    await BookRepository.update_book_availability(universal_id, False, "2025-01-01")
    updated_book = await BookRepository.get_book_by_universal_id(universal_id)
    assert updated_book["is_available"] is False


# test get unavailable books
@pytest.mark.asyncio
async def test_get_unavailable_books(mock_book_collection):
    unavailable_books = await BookRepository.get_unavailable_books(1, 10)
    print(unavailable_books) 
    assert len(unavailable_books) > 0