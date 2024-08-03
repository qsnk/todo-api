from datetime import datetime
from pydantic import BaseModel


class Todo(BaseModel):
    title: str
    description: str | None = None