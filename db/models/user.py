from sqlalchemy import Column, Boolean, ForeignKey, Integer, String
from sqlalchemy.sql import expression

from db.db_setup import Base
from db.models.mixins import Timestamp
from sqlalchemy.orm import relationship

class User(Base, Timestamp):
    __tablename__ ='users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index= True, nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    is_active = Column(Boolean, server_default=expression.true(), nullable=False)

    #This allows you to access the user directories 
    #The back_populate name has to be the name of the field on the Directory class that has this relationship and vise vers
    directory = relationship("Directory", back_populates="creator") 