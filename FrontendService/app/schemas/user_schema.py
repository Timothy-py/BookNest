

from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserEnrollSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    
    class Config:
        orm_mode = True  # for compatibility with SQLAlchemy


class UserSchema(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    created_at: datetime

    class Config:
        orm_mode = True 