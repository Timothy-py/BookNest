from datetime import date
from typing import Annotated, List


from pydantic import BaseModel, Field, BeforeValidator


# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class AddBook(BaseModel):
    title: str = Field(..., min_length=1, max_length=250)
    author: str = Field(..., min_length=1, max_length=250)
    publisher: str = Field(..., min_length=3, max_length=250)
    category_universal_id: str 
    is_available: bool = Field(default=True)
    available_date: date | None = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Alchemist",
                "author": "Paulo Coelho",
                "publisher": "Goodreads",
                "category_universal_id": "5bf5bb1b-2527-4505-9ec7-a203299d6ecd"
            }
        }

class BookResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    universal_id: str
    title: str
    author: str
    publisher: str
    category_universal_id: str
    is_available: bool
    available_date: date | None