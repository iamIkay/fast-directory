from fastapi import Depends
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_async_engine(os.getenv('DATABASE_URL'))

SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

async def get_db():
    async with SessionLocal() as db:
        try:
            yield db
        finally:
           await db.close()

db_dependency = Annotated[SessionLocal, Depends(get_db)]


