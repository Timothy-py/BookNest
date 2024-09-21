

from typing import List
from pydantic import BaseModel


class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    category_id: int
    quantity: int
    is_available: bool
    
    class Config:
        from_attributes = True  # for compatibility with SQLAlchemy
        
        
class PaginatedBookResponse(BaseModel):
    books: List[BookSchema]
    page: int
    size: int