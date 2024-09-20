from app.schemas.user_schema import UserEnrollSchema
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.repositories.user_repository import UserRepository
from app.core.dependencies import RabbitMQClient

class UserService:
    async def enroll_user(db: AsyncSession, producer:RabbitMQClient, data:UserEnrollSchema):
        try:
            new_user = await UserRepository.create_user(db, data)
        except sqlalchemy.exc.IntegrityError:
            raise HTTPException(status_code=409, detail="Email already exists")
        else:
            await producer.publish("user_enroll", data.model_dump_json())
            return new_user