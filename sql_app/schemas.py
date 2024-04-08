from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    """
    TaskBase is a Pydantic model that defines the fields that are common to both the TaskCreate and Task models.

    Attributes:
    - title (str): The title of the task.
    - description (str): The description of the task.
    """

    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    """
    TaskCreate is a Pydantic model that defines the fields required to create a new task. It inherits from TaskBase and
    adds no additional fields.
    """
    pass


class Task(TaskBase):
    """
    Task is a Pydantic model that defines the fields for a task entity. It inherits from TaskBase and adds id, owner_id
    and fields:
    """
    id: int
    owner_id: int
    state: int

    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    """
    UserBase is a Pydantic model that defines the fields that are common to both the UserCreate and User models.
    """
    name: str
    email: str


class UserCreate(UserBase):
    """
    UserCreate is a Pydantic model that defines the fields required to create a new user. It inherits from UserBase and
    adds the password field:
    """
    password: str


class User(UserBase):
    """
    User is a Pydantic model that defines the fields for a user entity. It inherits from UserBase and adds the id,
    is_active and items fields:
    """
    id: int
    is_active: bool
    items: list[Task] = []

    model_config = ConfigDict(from_attributes=True)
