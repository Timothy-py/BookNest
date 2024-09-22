


from fastapi import APIRouter, status, Query


from app.schemas.book_schema import BookSchema, PaginatedBookResponse
from app.services.book_service import BookService


book_router = APIRouter(prefix="/api/v1/books", tags=["Books"])


# List all books | Paginated
@book_router.get("/", response_model=PaginatedBookResponse, status_code=status.HTTP_200_OK)
async def list_books(page:int=Query(1, ge=1), size:int=Query(10, ge=1, le=100)):
    return await BookService.list_books(page, size)

# Get a book by ID
@book_router.get("/{id}", response_model=BookSchema, status_code=status.HTTP_200_OK)
async def get_book_by_id(id: int):
    return await BookService.get_book_by_id(id)
