from datetime import datetime
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    title: str
    description: str
    created_at: datetime
    owner_id: int