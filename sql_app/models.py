from pydantic import Field
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, index=True)
    name = Column(String(100))
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner")


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), index=True)
    description = Column(String(100), index=True)
    state = Column(Integer, default=0)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="tasks")
