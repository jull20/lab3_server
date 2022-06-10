from fastapi import APIRouter, HTTPException, Query, UploadFile, status, Path, Depends
from sqlalchemy.orm import Session

from v1.products.schema import ResponseProduct, ResponseSuccess
from core.settings.database import get_db
from v1.user.schema import UserSession
from core.utils.permissions import get_auth_user_from_session, get_admin_user_from_session

from v1.products.controller import *


router = APIRouter(prefix='/products', tags=['products'])


@router.get(
    path='/',
    summary='Получение списка все товаров',
    response_model=list[ResponseProduct],
)
async def get_all_products(
    db: Session = Depends(get_db)
):
    return await get_all_products_service(db)


@router.post(
    path='/',
    summary='Создание нового объекта товара',
    response_model=ResponseSuccess,
    responses={} # TODO: something wrong
)
async def create_new_product(
    product_name: str = Query(
        description='Название товара',
        example='AirPods Max'
    ),
    product_photo: UploadFile | None = None,
    price: float = Query(
        description='Цена товара',
        example=14.99,
        gt=0
    ),
    amount: int = Query(
        description='Начальное количество товара',
        example=30,
        gt=0
    ),
    user: UserSession = Depends(get_admin_user_from_session),
    db: Session = Depends(get_db)
):
   return await create_product_service(db, user, product_name, product_photo, price, amount)


@router.get(
    path='/{productId}',
    summary='Получение одного товара, по его id',
    response_model=ResponseProduct,
    responses={} # TODO: if wrong id 4xx response
)
async def get_product_by_id(
    productId: int = Path(
        description='Уникальный идентификатор товара',
        example=1,
        ge=1,
    ),
    db: Session = Depends(get_db)
):
    return await get_product_by_id_service(db, productId)


@router.post(
    path='/{productId}/rate',
    summary='Оставление рейтинга для товара от активного пользоваля',
    response_model=ResponseSuccess,
    responses={} # TODO: you have been voted yet
)
async def set_rate_to_product_by_id(
    productId: int = Path(
        description='Уникальный идентификатор товара',
        example=1,
        ge=1,
    ),
    rate_value: float = Query(
        description='Значение рейтинга продукта (от 1 до 5)',
        example=4,
        ge=1.0,
        le=5.0
    ),
    user: UserSession = Depends(get_auth_user_from_session),
    db: Session = Depends(get_db)
):
    return await post_product_rate_by_id(db, user, productId, rate_value)


@router.post(
    path='/{productId}/buy',
    summary='Оформление заказа выбранного товара',
    response_model=ResponseSuccess,
    responses={} # TODO: amount > remaind
)
async def buy_product_by_id(
    productId: int = Path(
        description='Уникальный идентификатор товара',
        example=1,
        ge=1,
    ),
    amount: int = Query(
        description='Количество товара к покупке',
        example=2,
        ge=1
    ),
    user: UserSession = Depends(get_auth_user_from_session),
    db: Session = Depends(get_db)
):
    return await post_product_buy_by_id(db, user, productId, amount)