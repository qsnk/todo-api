from models.permission import Permission
from models.todo import Todo
from sqlalchemy.orm import Session


def get_all_permissions(db: Session, user_id: int):
    try:
        permissions = db.query(Permission).filter(Permission.user_id == user_id).all()
        if not permissions:
            return {'message': 'permissions not found'}

    except Exception as e:
        return {'message': str(e)}

    return {'permissions': permissions}


def get_permission(db: Session, id: int):
    try:
        permission = db.query(Permission).filter(Permission.id == id).first()
        if not permission:
            return {'message': 'permission not found'}

    except Exception as e:
        return {'message': str(e)}

    return permission


def new_permission(db: Session, todo_id: int, creator_id: int, user_id: int):
    try:
        creator = db.query(Todo).filter(Todo.creator_id == creator_id).first()
        if not creator:
            return {'message': 'you dont have permission to edit permission to this todo'}

        permission = Permission(
            user_id=user_id,
            todo_id=todo_id,
            can_view=True,
            can_edit=True,
            can_delete=False
        )

        db.add(permission)
        db.commit()
        db.refresh(permission)

    except Exception as e:
        return {'message': str(e)}

    return permission


def return_permission(db: Session, todo_id: int, user_id: int):
    try:
        permission = db.query(Permission).filter(
            Permission.todo_id == todo_id,
            Permission.user_id == user_id
        ).first()

        if not permission:
            return {'message': 'Permission not found'}

        permission.can_view = False
        permission.can_edit = False
        permission.can_delete = False

        db.commit()
        db.refresh(permission)

    except Exception as e:
        return {'message': str(e)}

    return permission