from models.user import User
from sqlalchemy.orm import Session
from dto import user as UserDto
from hash_password import hash_password, verify_password


def get_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, data: UserDto.User):
    username = data.username
    password = data.password
    hashed_password = hash_password(password)

    if not verify_password(password, hashed_password):
        return {'message': 'password hashing error'}

    if get_username(db, username):
        return {'message': 'username already exists'}

    user = User(username=username, password=hashed_password)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        return {'message': str(e)}
    return {'user': user}


def get_user(db: Session, id: int):
    return db.query(User).filter(User.id == id).first()


def update_user(db: Session, id: int, data: UserDto.User):
    user = db.query(User).filter(User.id == id).first()
    username = data.username

    if get_username(db, username):
        return {'message': 'username already exists'}

    user.username = username

    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        return {'message': str(e)}
    return {'user': user}


def delete_user(db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    if user:
        db.delete(user)
        db.commit()
    return user