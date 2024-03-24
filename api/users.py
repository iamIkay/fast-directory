import fastapi
from fastapi import HTTPException
from typing import List
from db.db_setup import db_dependency 
from api.utils import users
from pydantic_schemas.user import UserModel, UserCreateModel, UserUpdateModel
from http import HTTPStatus

router = fastapi.APIRouter()

@router.get('/users', response_model=List[UserModel])
async def read_users(db: db_dependency):
    result = await users.get_users(db)

    return result


@router.post('/users', status_code=HTTPStatus.CREATED)
async def write_user(db: db_dependency, user: UserCreateModel):
    db_user = await users.get_user_by_email(db=db, email= user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email is already registered")
    
    return await users.create_user(db=db, user= user)


@router.get('/users/{user_id}', response_model=UserModel)
async def read_single_user(user_id: int, db: db_dependency):
    result = await users.get_user_by_id(db=db, id= user_id)

    return result

@router.patch('/users/{user_id}', response_model=UserModel)
async def update_user(user_id: int, db: db_dependency, data: UserUpdateModel):
    result = await users.update_user(db=db,id= user_id, data=data)

    return result

@router.delete('/users/{user_id}', status_code=HTTPStatus.NO_CONTENT)
async def update_user(user_id: int, db: db_dependency):
    result = await users.delete_user(db=db,id= user_id)

    return result

