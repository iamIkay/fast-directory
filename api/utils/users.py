from sqlalchemy.ext.asyncio import AsyncSession,async_sessionmaker
from sqlalchemy.future import select
from datetime import datetime

from db.models.user import User
from pydantic_schemas.user import UserCreateModel
from db.db_setup import db_dependency



async def get_users(db: async_sessionmaker[AsyncSession]):
    statement= select(User).order_by(User.id)

    result = await db.execute(statement)

    return result.scalars()


async def get_user_by_email(db: async_sessionmaker[AsyncSession], email: str):
    statement= select(User).filter_by(email=email)

    result = await db.execute(statement)
    
    return result.scalars().one_or_none()

async def create_user(db: async_sessionmaker[AsyncSession], user: UserCreateModel):

    db_user = User(email=user.email, username = user.username)

    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)    #Before adding this line, I was getting an empty map when I returned db_user
    return db_user




async def get_user_by_id(db: async_sessionmaker[AsyncSession], id:int):

    db_user =  select(User).filter_by(id=id)

    result = await db.execute(db_user)

    return result.scalars().one_or_none()


async def update_user(db: db_dependency, id:int, data):
    db_user = await get_user_by_id(db, id)
    
    db_user.username = db_user.username if data.username is None else data.username
    db_user.email = db_user.email if data.email is None else data.email
    #db_user.updated_at = datetime.now()

    await db.commit()
    await db.refresh(db_user)
    return db_user


async def delete_user(db: async_sessionmaker[AsyncSession], id: int ):
    db_user = await get_user_by_id(db=db, id=id)

    await db.delete(db_user)
    await db.commit()

    return {}
