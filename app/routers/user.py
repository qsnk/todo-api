from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import connect_db
from services import user as UserService
from dto import user as UserDto

router = APIRouter()


@router.post('/', tags=['user'])
async def create_user(data: UserDto.User = None, db: Session = Depends(connect_db)):
    return UserService.create_user(db=db, data=data)


@router.get('/{id}', tags=['user'])
async def get_user(id: int = None, db: Session = Depends(connect_db)):
    return UserService.get_user(db=db, id=id)


@router.put('/{id}', tags=['user'])
async def update_user(id: int = None, data: UserDto.User = None, db: Session = Depends(connect_db)):
    return UserService.update_user(db=db, id=id, data=data)


@router.delete('/{id}', tags=['user'])
async def delete_user(id: int = None, db: Session = Depends(connect_db)):
    return UserService.delete_user(db=db, id=id)