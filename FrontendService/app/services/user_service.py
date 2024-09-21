import json
import uuid


import sqlalchemy
from fastapi import HTTPException


from app.core.database import get_session
from app.models.user_model import User
from app.schemas.user_schema import UserEnrollSchema
from app.core.dependencies import RabbitMQClient

class UserService:
    async def enroll_user(producer:RabbitMQClient, data:UserEnrollSchema):
        try:
            universal_id = str(uuid.uuid4())
            async with get_session() as session:
                new_user = User(email=data.email, first_name=data.first_name, last_name=data.last_name, universal_id=universal_id)
                session.add(new_user)
                await session.commit()
                await session.refresh(new_user)
        except sqlalchemy.exc.IntegrityError:
            raise HTTPException(status_code=409, detail="Email already exists")
        else:
            # Update the data to include the universal_id
            data_with_universal_id = data.model_dump()
            data_with_universal_id["universal_id"] = universal_id
            await producer.publish("user_enroll", json.dumps(data_with_universal_id))
            return new_user