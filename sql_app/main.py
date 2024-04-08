from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/",tags=["User"], response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/",tags=["User"], response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/{user_id}/tasks/",tags=["Task"], response_model=schemas.Task)
def create_task_for_user(
        user_id: int,
        item: schemas.TaskCreate,
        db: Session = Depends(get_db)
):
    return crud.create_user_task(db=db, task=item, user_id=user_id)


@app.get("/users/{user_id}/tasks/",tags=["Task"], response_model=list[schemas.Task])
def read_tasks_by_user(user_id: int, db: Session = Depends(get_db)):
    tasks = crud.get_tasks_by_user(db, user_id=user_id)
    return tasks




@app.put("/tasks/{task_id}", tags=["Task"], response_model=schemas.Task)
def update_task_state(task_id: int, state: int, db: Session = Depends(get_db)):
    return crud.update_task_state(db=db, task_id=task_id, state=state)


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# @app.post("/tasks/", response_model=schemas.Task)
# def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
#     return crud.create_task(db=db, task=task)

# @app.get("/tasks/", response_model=list[schemas.Task])
# def read_task(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     tasks = crud.get_tasks(db, skip=skip, limit=limit)
#     return tasks


# @app.get("/tasks/{task_id}", response_model=schemas.Task)
# def read_task(task_id: int, db: Session = Depends(get_db)):
#     db_task = crud.get_task(db, task_id=task_id)
#     if db_task is None:
#         raise HTTPException(status_code=404, detail="Task not found")
#     return db_task