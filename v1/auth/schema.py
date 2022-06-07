from pydantic import BaseModel, Field


class ResponseSuccess(BaseModel):
    detail: str = Field(default='Success')