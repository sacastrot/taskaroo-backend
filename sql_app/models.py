"""
This module contains the SQLAlchemy model classes for the database entities.

SQLAlchemy is an Object-Relational Mapping (ORM) library for Python that provides a way to
interact with databases using Python objects.

"""

# Third-party imports
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# Local imports (project-specific)
from .database import Base

class User(Base):
    """
    Represents a user entity in the database.

    Attributes:
    - id (int): The unique identifier for the user (primary key).
    - email (str): The email address of the user (unique).
    - name (str): The name of the user.
    - hashed_password (str): The hashed password of the user.
    - is_active (bool): Indicates whether the user account is active (default is True).
    - tasks (relationship): One-to-many relationship with Task entities, representing tasks owned by the user.

    """

    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True, index=True)
    name = Column(String(100))
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

    tasks = relationship("Task", back_populates="owner")


class Task(Base):

    """
    Represents a task entity in the database.

    Attributes:
    - id (int): The unique identifier for the task (primary key).
    - title (str): The title of the task.
    - description (str): The description of the task.
    - state (int): The state of the task (default is 0).
    - owner_id (int): The id of the user who owns the task.
    - owner (relationship): Many-to-one relationship with User entity, representing the user who owns the task.

    """

    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), index=True)
    description = Column(String(100), index=True)
    state = Column(Integer, default=0)
    owner_id = Column(Integer, ForeignKey("user.id"))

    owner = relationship("User", back_populates="tasks")
