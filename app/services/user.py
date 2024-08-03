from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from database import connect_db
from models.user import User
from sqlalchemy.orm import Session
from dto import user as UserDto
from hash_password import hash_password, verify_password
from jwt_auth import decode_access_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


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


def get_current_user(db: Session = Depends(connect_db), token: str = Depends(oauth2_scheme)):
    return decode_access_token(db=db, token=token)


def update_user(db: Session, id: int, data: UserDto.User):
    try:
        user = db.query(User).filter(User.id == id).first()
        username = data.username

        if get_username(db, username):
            return {'message': 'username already exists'}

        user.username = username

        db.commit()
        db.refresh(user)

    except Exception as e:
        return {'message': str(e)}

    return {'user': user}


def delete_user(db: Session, id: int):
    try:
        user = db.query(User).filter(User.id == id).first()
        if user:
            db.delete(user)
            db.commit()
    except Exception as e:
        return {'message': str(e)}

    return user