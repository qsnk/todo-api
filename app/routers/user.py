from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from database import connect_db
from services import user as user_service
from dto import user as UserDto


router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")


@router.get('/me', tags=['Users'], response_model=UserDto.UserOut)
async def get_current_user(current_user: UserDto.User = Depends(user_service.get_current_user)):
    return current_user


@router.post('/new', tags=['Users'])
async def create_user(db: Session = Depends(connect_db), data: UserDto.User = None):
    return user_service.create_user(db=db, data=data)


@router.get('/{id}', tags=['Users'])
async def get_user(db: Session = Depends(connect_db), id: int = None):
    return user_service.get_user(db=db, id=id)


@router.put('/{id}', tags=['Users'])
async def update_user(db: Session = Depends(connect_db), id: int = None, data: UserDto.User = None):
    return user_service.update_user(db=db, id=id, data=data)


@router.delete('/{id}', tags=['Users'])
async def delete_user(db: Session = Depends(connect_db), id: int = None):
    return user_service.delete_user(db=db, id=id)