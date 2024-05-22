# Third-party imports
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

# Local imports (project-specific)
from . import crud, models, schemas
from .database import SessionLocal, engine

# Create the database tables
models.Base.metadata.create_all(bind=engine)

# Create the FastAPI app
app = FastAPI()

# Add CORS middleware to allow requests from the frontend
origins = ['*']


# Add CORS middleware to allow requests from the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    """
    Dependency to get a database session.

    Args:
    - None

    Returns:
    - Session: A SQLAlchemy session to the database.

    Yields:
    - Session: A SQLAlchemy session to the database.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", tags=["User"], response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Creates a new user in the database.

    Args:
    - user (schemas.UserCreate): The user data to create.
    - db (Session): The database session.

    Returns:
    - models.User: The created user object.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", tags=["User"], response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Retrieves a list of users from the database.

    Args:
    - skip (int): The number of users to skip.
    - limit (int): The number of users to retrieve.
    - db (Session): The database session.

    Returns:
    - list[models.User]: A list of user objects.
    """
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/{user_id}/tasks/", tags=["Task"], response_model=schemas.Task)
def create_task_for_user(

        user_id: int,
        item: schemas.TaskCreate,
        db: Session = Depends(get_db)
):
    """
    Creates a new task for a user in the database.

    Args:
    - user_id (int): The user id.
    - item (schemas.TaskCreate): The task data to create.
    - db (Session): The database session.

    Returns:
    - models.Task: The created task object.
    """
    return crud.create_user_task(db=db, task=item, user_id=user_id)


@app.get("/users/{user_id}/tasks/", tags=["Task"], response_model=list[schemas.Task])
def read_tasks_by_user(user_id: int, db: Session = Depends(get_db)):
    """
    Retrieves a list of tasks for a user from the database.

    Args:
    - user_id (int): The user id.
    - db (Session): The database session.
    
    Returns:
    - list[models.Task]: A list of task objects.
    """
    tasks = crud.get_tasks_by_user(db, user_id=user_id)
    return tasks


@app.put("/tasks/{task_id}", tags=["Task"], response_model=schemas.Task)
def update_task_state(task_id: int, state: int, db: Session = Depends(get_db)):
    """
    Updates the state of a task in the database.

    Args:
    - task_id (int): The task id.
    - state (int): The new state of the task.
    - db (Session): The database session.

    Returns:
    - models.Task: The updated task object.
    """
    return crud.update_task_state(db=db, task_id=task_id, state=state)
