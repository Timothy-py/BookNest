
from datetime import date
from typing import Annotated, List
from pydantic import BaseModel, BeforeValidator, EmailStr, Field


PyObjectId = Annotated[str, BeforeValidator(str)]


class UserSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    universal_id: str
    email: str
    first_name: str
    last_name: str
    borrowed_books: list | None = []
    

class PaginatedUserResponseSchema(BaseModel):
    users: List[UserSchema]
    page: int
    size: int


class BorrowedBookSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    book_universal_id: str
    borrower_universal_id: str
    borrowed_date: date
    return_date: date
    returned: bool
    book: dict

class UserWithBorrowedBooksSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    universal_id: str
    email: str
    first_name: str
    last_name: str
    borrowed_books: List[BorrowedBookSchema]

class PaginatedUsersResponse(BaseModel):
    users: List[UserWithBorrowedBooksSchema]
    page: int
    size: int