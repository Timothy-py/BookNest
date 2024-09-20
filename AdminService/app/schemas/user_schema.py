
from typing import Annotated, List
from pydantic import BaseModel, BeforeValidator, EmailStr, Field


PyObjectId = Annotated[str, BeforeValidator(str)]

class UserEnrollSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str


class UserSchema(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: str
    first_name: str
    last_name: str
    

class PaginatedUserResponseSchema(BaseModel):
    users: List[UserSchema]
    page: int
    size: int