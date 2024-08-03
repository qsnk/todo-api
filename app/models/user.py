from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import base as Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

    todo = relationship('Todo', back_populates='user')
    permissions = relationship('Permission', back_populates='user')