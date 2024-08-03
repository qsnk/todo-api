from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import base as Base


class Permission(Base):
    __tablename__ = 'permissions'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    todo_id = Column(Integer, ForeignKey('todos.id'))
    can_view = Column(Boolean)
    can_edit = Column(Boolean)
    can_delete = Column(Boolean)

    user = relationship('User', back_populates='permissions')
    todo = relationship('Todo', back_populates='permissions')