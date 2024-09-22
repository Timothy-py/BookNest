

from app.repositories.user_repository import UserRepository


class UserService:
    async def enroll_user(data: dict):
        new_user = await UserRepository.add_user(data)
        
    async def get_users(page:int, size:int):
        # Calculate how many users to skip
        skip = (page - 1) * size

        users = await UserRepository.get_users(skip, size)
        
        return {
            "users": users,
            "page": page,
            "size": size,
        }