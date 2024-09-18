from typing import Annotated, List


from pydantic import BaseModel, Field, BeforeValidator


# Represents an ObjectId field in the database.
# It will be represented as a `str` on the model so that it can be serialized to JSON.
PyObjectId = Annotated[str, BeforeValidator(str)]

class AddBook(BaseModel):
    title: str = Field(..., min_length=3, max_length=250)
    description: str = Field(..., min_length=3, max_length=250)
    author: str = Field(..., min_length=3, max_length=250)
    publisher: str = Field(..., min_length=3, max_length=250)
    category_ids: List[str] = Field(..., min_items=1)
    quantity: int = Field(..., gt=0)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Alchemist",
                "description": "The Alchemist is a novel by the English author Paulo Coelho. It was first published in 1988 and has since become one of the most popular novels in the world.",
                "author": "Paulo Coelho",
                "publisher": "Goodreads",
                "category_ids": ["64dfc2a7e913c97fdbcbbf2a"],
                "quantity": 5
            }
        }

class BookResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    description: str
    author: str
    publisher: str
    category_ids: List[str]
    quantity: int
    # created_at: datetime
    # updated_at: datetime