

from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserEnrollSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    
    class Config:
        from_attributes = True  # for compatibility with SQLAlchemy


class UserSchema(BaseModel):
    id: int
    universal_id: str
    email: str
    first_name: str
    last_name: str
    created_at: datetime

    class Config:
        from_attributes = True 