from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field
from db.models.mixins import Timestamp

#Schema for returning a user
class UserModel(BaseModel):
    id: int
    email:str
    username: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode: True


#Schema for creating a user
class UserCreateModel(BaseModel):
    email: str
    username: str

    class Config:
        orm_mode: True

    
#Schema for updating a user
class UserUpdateModel(BaseModel):
    email: Optional[str]=None
    username: Optional[str]=None
    updated_at: Optional[datetime] = datetime.now()

    class Config:
        orm_mode: True

    
