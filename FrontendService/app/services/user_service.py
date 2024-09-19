from app.schemas.user_schema import UserEnrollSchema
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import UserRepository


class UserService:
    async def enroll_user(db: AsyncSession, data:UserEnrollSchema):
        new_user = await UserRepository.create_user(db, data)
        return new_user