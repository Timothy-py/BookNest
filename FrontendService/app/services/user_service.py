from app.core.database import get_session
from app.models.user_model import User
from app.schemas.user_schema import UserEnrollSchema
import sqlalchemy
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.core.dependencies import RabbitMQClient

class UserService:
    async def enroll_user(producer:RabbitMQClient, data:UserEnrollSchema):
        try:
            async with get_session() as session:
                new_user = User(email=data.email, first_name=data.first_name, last_name=data.last_name)
                session.add(new_user)
                await session.commit()
                await session.refresh(new_user)
        except sqlalchemy.exc.IntegrityError:
            raise HTTPException(status_code=409, detail="Email already exists")
        else:
            await producer.publish("user_enroll", data.model_dump_json())
            return new_user