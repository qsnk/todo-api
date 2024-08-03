from models.permission import Permission
from models.todo import Todo
from sqlalchemy.orm import Session
from dto import permission as permission_dto


def new_permission(db: Session, permission: permission_dto.Permission, todo_id: int, user_id: int):
    try:
        creator = db.query(Todo.creator_id).filter(Todo.id == todo_id).scalar()
        if creator != user_id:
            return {'message': 'you dont have permission to edit permission to this todo'}

        permission = db.query(Permission).filter(
            Permission.todo_id == todo_id,
            Permission.user_id == permission.user_id
        ).first()

        if permission:
            permission.can_view = True
            permission.can_edit = True

        db.add(permission)
        db.commit()
        db.refresh(permission)
    except Exception as e:
        return {'message': str(e)}

    return permission


# def return_permission(db: Session, permission: permission_dto.Permission):
#     try:
#         creator = db.query(Todo.creator_id).filter(Todo.id == todo_id).scalar()
#         if creator != user_id:
#             return {'message': 'you dont have permission to edit permission to this todo'}
#
#         permission = db.query(Permission).filter(
#             Permission.todo_id == todo_id,
#             Permission.user_id == permission.user_id
#         ).first()
#
#         if permission:
#             permission.can_view = True
#             permission.can_edit = True
#
#         db.add(permission)
#         db.commit()
#         db.refresh(permission)
#     except Exception as e:
#         return {'message': str(e)}
#
#     return permission