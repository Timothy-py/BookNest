from fastapi import APIRouter, status


user_router = APIRouter(prefix="/api/v1/user", tags=["User"])


@user_router.get("/", status_code=status.HTTP_200_OK)
async def get_user():
    return {"message": "Hello World"}