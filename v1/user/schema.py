from pydantic import BaseModel, Field


class ResponseIsAdmin(BaseModel):
    value: str = Field(default=False)