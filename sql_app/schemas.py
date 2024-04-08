from pydantic import BaseModel, ConfigDict


class TaskBase(BaseModel):
    title: str
    description: str | None = None


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int
    owner_id: int
    state: int

    model_config = ConfigDict(from_attributes=True)


class UserBase(BaseModel):
    name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Task] = []

    model_config = ConfigDict(from_attributes=True)
