import fastapi
from .utils.directory import get_directories, create_directory, get_user_dir,get_directory_creator
from typing import List
from pydantic_schemas.directory import Directory, DirectoryCreate
from db.db_setup import db_dependency
from pydantic_schemas.user import UserModel


router = fastapi.APIRouter()


@router.get('/directories', response_model=List[Directory])
async def read_directories(db: db_dependency):
    result = await get_directories(db=db)

    return result


@router.post('/directories', response_model=Directory)
async def write_directory(db: db_dependency, data: DirectoryCreate):
    result = await create_directory(db=db, data=data)

    return result

@router.get('/directories/{user_id}', response_model=List[Directory])
async def get_user_directories(db: db_dependency, user_id: int):
    result = await get_user_dir(db=db, id=user_id)

    return result

@router.get('/directory/creator/{doc_id}', response_model=UserModel)
async def get_directory_crator(db:db_dependency, doc_id: int):
    result = await get_directory_creator(db=db, doc_id=doc_id)

    return result
