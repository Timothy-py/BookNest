
from pydantic import BaseModel, EmailStr


class UserEnrollSchema(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str