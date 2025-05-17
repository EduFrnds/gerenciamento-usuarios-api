from fastapi import APIRouter, Depends, Response, status, HTTPException
from app.adapters.repository.user import UserRepository
from app.adapters.schemas.user import UserCreateSchema, UserResponse

from app.logs.logging_config import configure_logging

logger = configure_logging()
router = APIRouter()


@router.post('/users')
async def create_user(user: UserCreateSchema, repository: UserRepository = Depends(UserRepository)):

    try:
        user = repository.register(user)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

@router.get('/users')
async def get_all_users(repository: UserRepository = Depends(UserRepository)):
    return repository.findall()


@router.get('/users/{user_id}')
async def get_user_by_id(
        user_id: int,
        repository: UserRepository = Depends(UserRepository)
):
    user = repository.find(id=user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    return UserResponse.model_validate(user)

@router.put('/users/{user_id}')
async def update_user(
        user_id: int,
        user: UserCreateSchema,
        repository: UserRepository = Depends(UserRepository)
):
    repository.update(uid=user_id, **user.dict())
    return user

@router.delete('/users/{user_id}')
async def delete_user(
        user_id: int,
        repository: UserRepository = Depends(UserRepository)
):
    try:
        repository.find(id=user_id)
        return {"message": "User deleted"}
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e),
        )