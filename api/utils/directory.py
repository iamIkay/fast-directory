from db.models.directory import Directory
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker
from pydantic_schemas.directory import DirectoryCreate
from .error_log import printLog
from db.models.user import User

async def get_directories(db: async_sessionmaker[AsyncSession]):
    statement = select(Directory).order_by(Directory.id)
    db_dirs = await db.execute(statement)
    return db_dirs.scalars()


async def create_directory(db: async_sessionmaker[AsyncSession], data: DirectoryCreate):
    
    dir = Directory(title=data.title, description=data.description, user_id=data.creator_id)
     
    printLog("USER ID "+ f'{dir.user_id}')
    db.add(dir)
    await db.commit()
    await db.refresh(dir)
    return dir

async def get_user_dir(db: async_sessionmaker[AsyncSession], id: int):
     statement = select(Directory).filter_by(user_id=id)

     result = await db.execute(statement)

     return result.scalars()

async def get_directory_creator(db: async_sessionmaker[AsyncSession], doc_id: int):
    #Get document
    statement = select(Directory).filter_by(id=doc_id)

    res = await db.execute(statement)

    doc = res.scalars().one_or_none()

    #Get creator id
    creator_id = doc.user_id

    #Get creator by Id
    cStatement = select(User).filter_by(id=creator_id)

    cResult = await db.execute(cStatement)

    creator = cResult.scalars().one_or_none()

    return creator