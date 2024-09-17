from fastapi import APIRouter, status


book_router = APIRouter(prefix="/api/v1/books", tags=["Books"])


@book_router.get("/", status_code=status.HTTP_200_OK)
async def add_book():
    return {"message": "Hello World"}