


from typing import Annotated
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, BeforeValidator, Field


PyObjectId = Annotated[str, BeforeValidator(str)]


class CategorySchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=250)
    description: str | None = Field(None, min_length=3, max_length=250)
    
    class Config:
        json_schema_extra = {
        "example": {
            "title": "Technology",
            "description": "Technology category",
        }
    }
        jsonable_encoder = {
            ObjectId: str   
        }


class CategoryResponse(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    universal_id: str
    title: str
    description: str | None
