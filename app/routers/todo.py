from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import connect_db
from dto import todo as todo_dto
from dto.user import UserOut
from services import todo as todo_service
from services.user import get_current_user

router = APIRouter()


@router.get('/', tags=['Todos'])
def get_all_todos(
        db: Session = Depends(connect_db),
        current_user: UserOut = Depends(get_current_user)
        ):
    return todo_service.get_all_todos(db=db, user_id=current_user.id)


@router.post('/new', tags=['Todos'])
def create_todo(
        db: Session = Depends(connect_db), data: todo_dto.Todo = None,
        current_user: UserOut = Depends(get_current_user)
        ):
    return todo_service.create_todo(db=db, data=data, creator_id=current_user.id)


@router.get('/{id}', tags=['Todos'])
def get_todo(
        db: Session = Depends(connect_db),
        id: int = None,
        current_user: UserOut = Depends(get_current_user)
        ):
    return todo_service.get_todo(db=db, id=id, user_id=current_user.id)


@router.put('/{id}', tags=['Todos'])
def update_todo(
        db: Session = Depends(connect_db),
        id: int = None,
        data: todo_dto.Todo = None,
        current_user: UserOut = Depends(get_current_user)
        ):
    return todo_service.update_todo(db=db, id=id, data=data, user_id=current_user.id)


@router.delete('/{id}', tags=['Todos'])
def delete_todo(
        db: Session = Depends(connect_db),
        id: int = None,
        current_user: UserOut = Depends(get_current_user)
        ):
    return todo_service.delete_todo(db=db, id=id, user_id=current_user.id)