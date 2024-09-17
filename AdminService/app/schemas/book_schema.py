

class AddBook(BaseModel):
    title: str = Field(..., min_length=3, max_length=250)
    description: str = Field(..., min_length=3, max_length=250)
    author: str = Field(..., min_length=3, max_length=250)
    publisher: str = Field(..., min_length=3, max_length=250)
    category_ids: List[str] = Field(..., min_items=1)
    quantity: int = Field(..., gt=0)

    class Config:
        schema_extra = {
            "example": {
                "title": "The Alchemist",
                "description": "The Alchemist is a novel by the English author Paulo Coelho. It was first published in 1988 and has since become one of the most popular novels in the world.",
                "author": "Paulo Coelho",
                "publisher": "Goodreads",
                "category_ids": ["64dfc2a7e913c97fdbcbbf2a"],
                "quantity": 5
            }
        }
