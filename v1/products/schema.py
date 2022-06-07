from pydantic import BaseModel, Field


class ResponseProduct(BaseModel):
    name: str = Field(default='AirPods Max')
    photo: str = Field(default='https://vk.com/good_photo.jpg')
    rate: float = Field(default=4.75)
    remaind: int = Field(default=26)
    price: float = Field(default=76.99)


class ResponseSuccess(BaseModel):
    detail: str = Field(default='Success')