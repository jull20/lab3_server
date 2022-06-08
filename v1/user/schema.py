from typing import NamedTuple
from pydantic import BaseModel, Field


class ResponseIsAdmin(BaseModel):
    value: str = Field(default=False)


class UserSession(NamedTuple):
    id: int
    username: str
    name: str
    email: str
    isAdmin: bool