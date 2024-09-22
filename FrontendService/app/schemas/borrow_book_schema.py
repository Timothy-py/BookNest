


from datetime import date
from pydantic import BaseModel


class BorrowBookSchema(BaseModel):
    user_id: int
    return_date: date
    

class BorrowBookResponseSchema(BaseModel):
    id: int
    borrower_universal_id: str
    book_universal_id: str
    return_date: date
    borrowed_date: date
    returned: bool