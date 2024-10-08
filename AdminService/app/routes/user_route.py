from fastapi import APIRouter, Query, status

from app.services.user_service import UserService
from app.schemas.user_schema import PaginatedUserResponseSchema, PaginatedUsersResponse


user_router = APIRouter(prefix="/api/v1/users", tags=["User"])


@user_router.get("/", response_model=PaginatedUserResponseSchema, status_code=status.HTTP_200_OK)
async def get_users(page:int=Query(1, ge=1), size: int = Query(10, ge=1, le=100)):
    return await UserService.get_users(page, size)

# Get users with borrowed books
@user_router.get("/borrowed_books",response_model=PaginatedUsersResponse, status_code=status.HTTP_200_OK)
async def get_users_with_borrowed_books(page:int=Query(1, ge=1), size: int = Query(10, ge=1, le=100)):
    return await UserService.get_users_with_borrowed_books(page, size)