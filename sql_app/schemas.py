"""
The schemas module contains Pydantic models that define the structure
of the data that is sent to and received from the API endpoints. These models are used to
validate the data and serialize it to and from JSON format.

Pydantic is a data validation and parsing library for Python that uses type annotations to define
the structure of the data. It provides a way to define data models with type hints and automatically
validate and serialize the data based on these models.
"""

# Third-party imports
from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    """
    TaskBase is a Pydantic model that defines the fields that are common to both the TaskCreate and Task models.

    Attributes:
    - title (str): The title of the task.
    - description (str): The description of the task.
    """

    title: str
    description: str


class TaskCreate(TaskBase):
    """
    TaskCreate is a Pydantic model that defines the fields required 
    to create a new task. It inherits from TaskBase and

    Attributes:
    - title (str): The title of the task.
    - description (str): The description of the task.

    """
    pass


class Task(TaskBase):
    """
    Task is a Pydantic model that defines the fields for a task entity. 
    It inherits from TaskBase and adds the id, owner_id, and state fields.

    Attributes:
    - id (int): The unique identifier for the task.
    - owner_id (int): The id of the user who owns the task.
    - state (int): The state of the task.

    """
    id: int
    owner_id: int
    state: int

    # ConfigDict is a Pydantic class that allows configuration settings to be defined as class attributes.
    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    """
    UserBase is a Pydantic model that defines the fields that are 
    common to both the UserCreate and User models.

    Attributes:
    - name (str): The name of the user.
    - email (str): The email address of the user.
    """
    name: str
    email: str


class UserCreate(UserBase):
    """
    UserCreate is a Pydantic model that defines the fields required to 
    create a new user.

    Attributes:
    - name (str): The name of the user.
    - email (str): The email address of the user.
    - password (str): The password of the user.

    """
    password: str


class User(UserBase):
    """
    User is a Pydantic model that defines the fields for a user entity.

    Attributes:
    - id (int): The unique identifier for the user.
    - is_active (bool): Indicates whether the user account is active.
    - items (list[Task]): A list of tasks owned by the user.

    """
    id: int
    is_active: bool
    items: list[Task] = []

    # ConfigDict is a Pydantic class that allows configuration settings to be defined as class attributes.
    model_config = ConfigDict(from_attributes=True)
