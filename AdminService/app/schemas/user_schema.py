
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