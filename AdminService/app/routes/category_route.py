

from fastapi import APIRouter, Depends, status

from app.core.dependencies import get_rabbitmq_client, RabbitMQClient
from app.services.category_service import CategoryService
from app.schemas.category_schema import CategoryResponse, CategorySchema


category_router = APIRouter(prefix="/api/v1/categories", tags=["Categories"])


# CREATE A CATEGORY
@category_router.post("/", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
async def create_category(category: CategorySchema, producer:RabbitMQClient = Depends(dependency=(get_rabbitmq_client))):
    return await CategoryService.create_category(category, producer)

# GET ALL CATEGORIES
@category_router.get("/", response_model=list[CategoryResponse], status_code=status.HTTP_200_OK)
async def get_categories():
    return await CategoryService.get_categories()