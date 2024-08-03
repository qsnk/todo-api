from pydantic import BaseModel


class Permission(BaseModel):
    user_id: int
    can_read: bool
    can_edit: bool
    can_delete: bool