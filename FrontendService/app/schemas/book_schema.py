

from datetime import date
from typing import List
from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    universal_id: str
    title: str
    author: str
    publisher: str
    category_universal_id: str
    is_available: bool
    available_date: date | None
    
    class Config:
        from_attributes = True  # for compatibility with SQLAlchemy
        
        
class PaginatedBookResponse(BaseModel):
    books: List[BookSchema]
    page: int
    size: int