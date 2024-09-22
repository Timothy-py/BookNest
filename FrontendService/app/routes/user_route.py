from fastapi import APIRouter, Depends, status

from app.services.user_service import UserService
from app.schemas.user_schema import UserEnrollSchema, UserSchema
from app.core.dependencies import get_rabbitmq_client, RabbitMQClient



user_router = APIRouter(prefix="/api/v1/users", tags=["Users"])


# Enroll User
@user_router.post(path="/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def enroll_user(user: UserEnrollSchema, producer:RabbitMQClient = Depends(get_rabbitmq_client)):
    return await UserService.enroll_user(producer, user)