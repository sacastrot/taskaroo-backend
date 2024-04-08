from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, name=user.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Task).offset(skip).limit(limit).all()


def create_user_task(db: Session, task: schemas.TaskCreate, user_id: int):
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks_by_user(db: Session, user_id: int):
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()


def get_task(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def update_task_state(db: Session, task_id: int, state: int):
    db.query(models.Task).filter(models.Task.id == task_id).update({"state": state})
    db.commit()
    return db.query(models.Task).filter(models.Task.id == task_id).first()
