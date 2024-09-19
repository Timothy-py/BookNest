
from sqlalchemy.ext.asyncio import AsyncSession


from app.models.user_model import User
from app.schemas.user_schema import UserEnrollSchema


class UserRepository:        
    async def create_user(db: AsyncSession, data: UserEnrollSchema) -> User:
        """create a new user"""
        new_user = User(email=data.email, first_name=data.first_name, last_name=data.last_name)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user
        