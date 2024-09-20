

from app.repositories.user_repository import UserRepository


class UserService:
    async def enroll_user(data: dict):
        new_user = await UserRepository.add_user(data)