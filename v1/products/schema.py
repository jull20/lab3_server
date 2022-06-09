from pydantic import BaseModel, Field


class ResponseProduct(BaseModel):
    id: int = Field(default=1, description='Идентификатор продукта')
    name: str = Field(default='AirPods Max')
    photo: str = Field(default='https://vk.com/good_photo.jpg')
    rate: float | None = Field(default=4.75, description='Средний рейтинг товара, может быть значение null - когда его еще не оценили')
    remaind: int = Field(default=26)
    price: float = Field(default=76.99)


class ResponseSuccess(BaseModel):
    detail: str = Field(default='Success')