


from typing import Annotated
from pydantic import BaseModel, BeforeValidator, Field


PyObjectId = Annotated[str, BeforeValidator(str)]


class CategorySchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=250)
    description: str = Field(..., optional=True, min_length=3, max_length=250)
    
    class Config:
        json_schema_extra = {
        "example": {
            "title": "Technology",
            "description": "Technology category",
        }
    }


class CategoryResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    title: str
    description: str
