from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    """
       Retrieves a user from the database by user ID.

       :param db: (Session): The database session.
       :param user_id: (int): The ID of the user to retrieve.

       :return models.User: The user object corresponding to the provided user ID.

       Example:
       >>> user = get_user(db, 123)
       >>> print(user.username)
       'example_user'
       """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
       Retrieves a user from the database by email address.

       :param db: (Session): The database session.
       :param email: (str): The email address of the user to retrieve.

       :return models.User: The user object corresponding to the provided email address.

       Example:
        >>> user = get_user_by_email(db, 'email@email.com')
        >>> print(user)
        '{
            "id": 1,
            "email": "email@email.com",
            "name": "example_user",
            "is_active": true,
            "items": []
        }'
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
        Retrieves a list of users from the database.

        :param db: (Session): The database session.
        :param skip: (int): The number of users to skip.
        :param limit: (int): The number of users to retrieve.

        :return list[models.User]: A list of user objects.

        Example:
        >>> users = get_users(db, 0, 10)
        >>> print(users)
        '[{
            "id": 1,
            "email": "email@email.com",
            "name": "example_user",
            "is_active": true,
            "items": []
        }, ...]'
    """

    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):

    """
    Creates a new user in the database.

    :param db:(Session): The database session.
    :param user:(schemas.UserCreate): The user data to create.

    :return models.User: The created user object.

    Example:

    >>> user_data = schemas.UserCreate(email="email@email.com", name="example_user", password="password")
    >>> create_user(db, user)
    >>> print(user.username)

    '{
        "id": 1,
        "email": "email@email.com",
        "name": "example_user",
        "is_active": true,
        "items": []
    }'

    """

    fake_hashed_password = user.password + "notReallyHashed"
    db_user = models.User(email=user.email, name=user.name, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_tasks(db: Session, skip: int = 0, limit: int = 100):

    """
    Retrieve a list of tasks from the database.

    :param db: (Session): The database session.
    :param skip: (int): The number of tasks to skip.
    :param limit: (int): The number of tasks to retrieve.

    :return: List[models.Task]: A list of task objects.

    Example:

    >>> tasks = get_tasks(db, 0, 10)
    >>> print(tasks)

    '[
        {
          "title": "string",
          "description": "string",
          "id": 0,
          "owner_id": 0,
          "state": 0
        },...,
    ]'

    """

    return db.query(models.Task).offset(skip).limit(limit).all()


def create_user_task(db: Session, task: schemas.TaskCreate, user_id: int):
    """
    Create a new task for a user in the database.

    :param db: (Session): The database session.
    :param task: (schemas.TaskCreate): The task data to create.
    :param user_id: (int): The ID of the user to create the task for.

    :return: models.Task: The created task object.

    Example:

    >>> task_db = schemas.TaskCreate(title="string", description="string")
    >>> create_user_task(db, task, 123)

    '{
        "title": "string",
        "description": "string",
        "id": 0,
        "owner_id": 0,
        "state": 0
    }'
    """
    db_task = models.Task(**task.dict(), owner_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_tasks_by_user(db: Session, user_id: int):

    """
    Retrieve a list of tasks from the database for a specific user.
    :param db: (Session): The database session.
    :param user_id: (int): The ID of the user to retrieve tasks for.

    :return: (List[models.Task]): A list of task objects.

    Example:
    >>> tasks = get_tasks_by_user(db, 123)
    >>> print(tasks)

    '[
        {
            "title": "string",
            "description": "string",
            "id": 0,
            "owner_id": 0,
            "state": 0
        },...,
    ]'
    """
    return db.query(models.Task).filter(models.Task.owner_id == user_id).all()


def get_task(db: Session, task_id: int):
    """
    Retrieve a task from the database by task ID.
    :param db: (Session): The database session.
    :param task_id: (int): The ID of the task to retrieve.

    :return: (models.Task): The task object corresponding to the provided task ID.

    Example:
    >>> task = get_task(db, 123)
    >>> print(task)

    '{
        "title": "string",
        "description": "string",
        "id": 0,
        "owner_id": 0,
        "state": 0
    }'
    """
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def update_task_state(db: Session, task_id: int, state: int):

    """
    Update the state of a task in the database.

    :param db: (Session): The database session.
    :param task_id: (int): The ID of the task to update.
    :param state: (int): The new state of the task.

    :return: (models.Task): The updated task object.

    Example:
    >>> task = update_task_state(db, 123, 1)
    >>> print(task)

    '{
        "title": "string",
        "description": "string",
        "id": 0,
        "owner_id": 0,
        "state": 1
    }'
    """
    db.query(models.Task).filter(models.Task.id == task_id).update({"state": state})
    db.commit()
    return db.query(models.Task).filter(models.Task.id == task_id).first()
