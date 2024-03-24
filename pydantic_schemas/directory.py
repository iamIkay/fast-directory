from pydantic import BaseModel
from typing import Optional


class Directory(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    user_id: int


class DirectoryCreate(BaseModel):
    title: str
    description: Optional[str] = None
    creator_id:int



