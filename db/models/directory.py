from sqlalchemy import Column, Boolean, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from ..db_setup import Base
from .mixins import Timestamp

class Directory(Base, Timestamp):

    __tablename__ = "directories"
    
    id=Column(Integer, unique=True, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    creator = relationship("User", back_populates="directory")

    