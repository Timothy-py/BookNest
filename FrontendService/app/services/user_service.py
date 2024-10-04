import json
import uuid


from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException


# from app.core.database import get_session
from app.core.database import database
from app.models.user_model import User
from app.schemas.user_schema import UserEnrollSchema
from app.core.dependencies import RabbitMQClient



class UserService:
    async def enroll_user(producer: RabbitMQClient, data: UserEnrollSchema):
        async with database.get_session() as session:
            new_user = User(email=data.email, first_name=data.first_name, last_name=data.last_name, universal_id=str(uuid.uuid4()))
            session.add(new_user)
            try:
                await session.commit()
                await session.refresh(new_user)
            except IntegrityError:
                raise HTTPException(status_code=409, detail="Email already exists")
            else:
                data_with_universal_id = data.model_dump()
                data_with_universal_id["universal_id"] = new_user.universal_id
                await producer.publish("user_enroll", json.dumps(data_with_universal_id))
                return new_user
        
    async def get_user_by_id(id: int) -> User:
        """Get a user by ID"""
        async with database.get_session() as session:
            result = await session.execute(select(User).filter(User.id == id))
            user = result.scalars().first()
        
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        return user
