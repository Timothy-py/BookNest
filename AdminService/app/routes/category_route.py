

from fastapi import APIRouter, status

from app.services.category_service import CategoryService
from app.schemas.category_schema import CategoryResponse, CategorySchema


category_router = APIRouter(prefix="/api/v1/categories", tags=["Categories"])


# CREATE A CATEGORY
@category_router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategorySchema):
    return await CategoryService.create_category(category)

# GET ALL CATEGORIES
@category_router.get("/", response_model=list[CategoryResponse], status_code=status.HTTP_200_OK)
async def get_categories():
    return await CategoryService.get_categories()