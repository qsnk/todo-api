from models.todo import Todo
from models.permission import Permission
from sqlalchemy.orm import Session
from sqlalchemy import desc
from dto import todo as todo_dto
from dto import user as user_dto

def get_all_todos(db: Session, user_id: int):
    try:
        permission = db.query(Permission).filter(
            Permission.user_id == user_id,
            Permission.can_view == True
        ).first()

        if not permission:
            return {'message': 'you dont have permission to view these todos'}

        todos = db.query(Todo).filter(Todo.creator_id == user_id).order_by(desc(Todo.created_at)).all()

        if not todos:
            return {'message': 'todos not found'}

    except Exception as e:
        return {'message': str(e)}

    return {'todos': todos}


def create_todo(db: Session, data: todo_dto.Todo, user: user_dto.UserOut):
    try:
        todo = Todo(
            title=data.title,
            description=data.description,
            created_at=data.created_at,
            creator_id=user.id,
        )
        db.add(todo)
        db.commit()
        db.refresh(todo)

        owner_permission = Permission(
            user_id=user.id,
            todo_id=todo.id,
            can_view=True,
            can_edit=True,
            can_delete=True,
        )
        db.add(owner_permission)
        db.commit()
        db.refresh(owner_permission)

    except Exception as e:
        return {'message': str(e)}

    return {'todo': todo}


def get_todo(db: Session, id: int, user_id: int):
    todo = db.query(Todo).filter(Todo.id == id).first()
    if not todo:
        return {'message': 'todo not found'}

    permission = db.query(Permission).filter(Permission.id == user_id).first()
    if not permission or not permission.can_view:
        return {'message': 'you dont have permission to view this todo'}

    return todo


def update_todo(db: Session, id: int, data: todo_dto.Todo, user_id: int):
    try:
        todo = db.query(Todo).filter(Todo.id == id).first()
        if not todo:
            return {'message': 'todo not found!'}

        permission = db.query(Permission).filter(
            Permission.todo_id == id,
            Permission.user_id == user_id
        ).first()

        if not permission:
            return {'message': 'permission not found'}

        if not permission.can_view or not permission.can_edit:
            return {'message': 'you dont have permission to edit this todo!'}

        todo.title = data.title
        todo.description = data.description
        db.commit()
        db.refresh(todo)

    except Exception as e:
        return {'message': str(e)}

    return todo


def delete_todo(db: Session, id: int, user_id: int):
    try:
        todo = db.query(Todo).filter(Todo.id == id).first()

        if not todo:
            return {'message': 'todo not found!'}

        creator = db.query(Todo.creator_id).filter(Todo.id == id).scalar()

        if creator != user_id:
            return {'message': 'you dont have permission to delete this todo!'}

        db.delete(todo)
        db.commit()

    except Exception as e:
        return {'message': str(e)}

    return todo