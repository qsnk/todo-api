from fastapi import APIRouter, Depends
from models.permission import Permission
from sqlalchemy.orm import Session
from database import connect_db
from dto import permission as permission_dto
from services import permission as permission_service


router = APIRouter()


@router.post("/new", tags=['Permissions'])
def new_permission(
        db: Session = Depends(connect_db),
        permission: permission_dto.Permission = None,
        todo_id: int = None,
        user_id: int = None
    ):
    return permission_service.edit_permission(
        db=db,
        permission=permission,
        todo_id=todo_id,
        user_id=user_id
    )