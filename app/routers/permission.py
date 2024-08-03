from fastapi import APIRouter, Depends
from sqlalchemy.sql.functions import current_user

from models.permission import Permission
from sqlalchemy.orm import Session
from database import connect_db
from dto import permission as permission_dto
from dto import user as user_dto
from services import permission as permission_service
from services.user import get_current_user

router = APIRouter()


@router.get('/', tags=['Permissions'])
def get_all_permissions(
        db: Session = Depends(connect_db),
        current_user: user_dto.UserOut = Depends(get_current_user)
        ):
    return permission_service.get_all_permissions(db=db, user_id=current_user.id)


@router.post("/new", tags=['Permissions'])
def new_permission(
        db: Session = Depends(connect_db),
        todo_id: int = None,
        current_user: user_dto.UserOut = Depends(get_current_user),
        user_id: int = None
    ):
    return permission_service.new_permission(
        db=db,
        todo_id=todo_id,
        creator_id=current_user.id,
        user_id=user_id
    )


@router.post('/{id}', tags=['Permissions'])
def return_permission(
        db: Session = Depends(connect_db),
        todo_id: int = None,
        user_id: int = None
        ):
    return permission_service.return_permission(db=db, todo_id=todo_id, user_id=user_id)